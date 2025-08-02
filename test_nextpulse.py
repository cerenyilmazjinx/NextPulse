# test_nextpulse.py
"""
Tests for NextPulse module.
"""

import unittest
from nextpulse import NextPulse

class TestNextPulse(unittest.TestCase):
    """Test cases for NextPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextPulse()
        self.assertIsInstance(instance, NextPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
