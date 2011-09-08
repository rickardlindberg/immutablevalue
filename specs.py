import unittest

from immutablevalue import ImmutableValue


class Point(ImmutableValue):

    FIELDS = {
        "x": 0,
        "y": 0,
    }

    def validate(self):
        if self.x is None:
            raise ValueError()


class Vector(ImmutableValue):

    FIELDS = {
        "x": 0,
        "y": 0,
    }


class DescribeImmutableValues(unittest.TestCase):

    def test_get_default_values_if_none_specified(self):
        self.assertEquals(0, Point().x)
        self.assertEquals(0, Point().y)

    def test_get_specified_values(self):
        p = Point(x=8)
        self.assertEquals(8, p.x)

    def test_can_not_contain_values_not_specified_in_fields(self):
        try:
            Point(z=4)
            self.fail("Was able to assign value not in fields.")
        except ValueError:
            pass

    def test_values_can_not_be_modified_in_place(self):
        try:
            p = Point(x=2)
            p.x = 3
            self.fail("Was able to modify value.")
        except ValueError:
            pass

    def test_values_can_not_be_deleted(self):
        try:
            p = Point(x=2)
            del p.x
            self.fail("Was able to delete value.")
        except ValueError:
            pass

    def test_values_can_be_modified_by_creating_a_new_object(self):
        p = Point(x=2)
        new_value = p.where(x=3)
        self.assertEquals(3, new_value.x)

    def test_it_keeps_old_values_when_modifying(self):
        p = Point(x=2, y=5)
        new_value = p.where(x=3)
        self.assertEquals(5, new_value.y)

    def test_when_modifying_values_a_new_object_is_created(self):
        p1 = Point(x=1)
        p2 = p1.where(x=3)
        self.assertFalse(p1 is p2)

    def test_values_can_be_validated_after_set(self):
        try:
            Point(x=None, y=4)
            self.fail("No validation occurred.")
        except ValueError:
            pass

    def test_are_equal_if_all_values_are_equal(self):
        self.assertEqual(Point(x=1, y=2), Point(x=1, y=2))

    def test_are_not_equal_if_all_values_are_not_equal(self):
        self.assertNotEqual(Point(x=0, y=2), Point(x=1, y=2))

    def test_are_not_equal_if_compared_to_other_object_with_same_fields(self):
        self.assertNotEqual(Point(x=0, y=2), Vector(x=0, y=2))

    def test_has_a_readable_repr(self):
        self.assertEquals("Point<y=2, x=1>", str(Point(x=1, y=2)))


if __name__ == "__main__":
    unittest.main()
