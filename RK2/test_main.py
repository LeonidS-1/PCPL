import unittest
from main_refactored import DataBase, Procedure, ProcedureDB, get_procedures_in_odd_databases, get_max_procedure_size_by_database, get_procedures_by_connections
class TestProcedures(unittest.TestCase):
    def setUp(self):
        self.dbs = [
            DataBase(1, 'db1'),
            DataBase(2, 'db2'),
            DataBase(3, 'db3')
        ]

        self.procedures = [
            Procedure(1, 'p1', 16, 1),
            Procedure(2, 'p2', 32, 1),
            Procedure(3, 'p3', 64, 2),
            Procedure(4, 'p4', 128, 2),
            Procedure(5, 'p5', 256, 3),
            Procedure(6, 'p6', 512, 3)
        ]

        self.dbs_to_procedures = [
            ProcedureDB(1, 1),
            ProcedureDB(1, 2),
            ProcedureDB(1, 3),
            ProcedureDB(2, 4),
            ProcedureDB(2, 5),
            ProcedureDB(2, 6),
            ProcedureDB(3, 1),
            ProcedureDB(3, 6)
        ]

    def test_get_procedures_in_odd_databases(self):
        result = get_procedures_in_odd_databases(self.dbs, self.procedures)
        expected = {'db1': ['p1', 'p2'], 'db3': ['p5', 'p6']}
        self.assertEqual(result, expected)

    def test_get_max_procedure_size_by_database(self):
        result = get_max_procedure_size_by_database(self.dbs, self.procedures)
        expected = {'db1': 32, 'db2': 128, 'db3': 512}
        self.assertEqual(result, expected)

    def test_get_procedures_by_connections(self):
        result = get_procedures_by_connections(self.dbs, self.procedures, self.dbs_to_procedures)
        expected = {
            'db1': ['p1', 'p2', 'p3'],
            'db2': ['p4', 'p5', 'p6'],
            'db3': ['p1', 'p6']
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()