import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "linked-lists" / "dual-sorted-list.cpp"

RECORDS = [
    ("Zoe", 150),
    ("Alice", 120),
    ("Mike", 180),
    ("Bob", 140),
    ("Emma", 130),
    ("David", 170),
    ("Olivia", 125),
    ("Chris", 160),
    ("Sophia", 115),
    ("James", 190),
    ("Liam", 145),
    ("Ava", 135),
    ("Noah", 175),
    ("Mia", 110),
    ("Ethan", 155),
]


class TestDualSortedList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.executable = Path(cls.temp_dir.name) / "dual-sorted-list"

        subprocess.run(
            [
                "clang++",
                "-std=c++17",
                "-Wall",
                "-Wextra",
                "-pedantic",
                str(SOURCE),
                "-o",
                str(cls.executable),
            ],
            check=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def test_sorting_by_name_and_weight(self):
        input_data = "".join(
            f"{name}\n{weight}\n"
            for name, weight in RECORDS
        )

        result = subprocess.run(
            [str(self.executable)],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5,
            check=True,
        )

        output = result.stdout

        name_section = output.split("Sorted by name:\n")[1]
        name_section = name_section.split("\nSorted by weight:\n")[0]

        weight_section = output.split("Sorted by weight:\n")[1]

        actual_names = [
            line.split(" - ")[0]
            for line in name_section.strip().splitlines()
        ]

        actual_weights = [
            float(line.rsplit(" - ", 1)[1])
            for line in weight_section.strip().splitlines()
        ]

        expected_names = sorted(name for name, _ in RECORDS)
        expected_weights = sorted(weight for _, weight in RECORDS)

        self.assertEqual(actual_names, expected_names)
        self.assertEqual(actual_weights, expected_weights)

    def test_duplicate_names_and_weights(self):
        records = [
            ("Alice", 120),
            ("Alice", 150),
            ("Bob", 120),
            ("Charlie", 150),
            ("David", 130),
            ("Emma", 140),
            ("Frank", 160),
            ("Grace", 110),
            ("Henry", 170),
            ("Ivy", 180),
            ("Jack", 190),
            ("Kate", 200),
            ("Liam", 210),
            ("Mia", 220),
            ("Noah", 230),
        ]

        input_data = "".join(
            f"{name}\n{weight}\n"
            for name, weight in records
        )

        result = subprocess.run(
            [str(self.executable)],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5,
            check=True,
        )

        name_section = result.stdout.split("Sorted by name:\n")[1]
        name_section = name_section.split("\nSorted by weight:\n")[0]

        weight_section = result.stdout.split("Sorted by weight:\n")[1]

        actual_names = [
            line.rsplit(" - ", 1)[0]
            for line in name_section.strip().splitlines()
        ]

        actual_weights = [
            float(line.rsplit(" - ", 1)[1])
            for line in weight_section.strip().splitlines()
        ]

        self.assertEqual(
            actual_names,
            sorted(name for name, _ in records)
        )

        self.assertEqual(
            actual_weights,
            sorted(weight for _, weight in records)
        )


if __name__ == "__main__":
    unittest.main()
