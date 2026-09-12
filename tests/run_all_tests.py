"""
Master Adversarial Test Runner
Executes full suite of empirical tests for Legal Claim Package Dossier & DB Insurance Architecture.
"""

import unittest
import sys
import os

# Set UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Add tests directory to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from test_adversarial_suite import TestAdversarialDossierSuite
from test_adversarial_deep_dive import TestAdversarialDeepDive
from test_statutory_financial_stress import TestStatutoryFinancialStress
from test_challenger_artifact_integrity import TestChallengerArtifactIntegrity
from test_harness_challenger_r3_1 import AdversarialStressTester

def run_master_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestAdversarialDossierSuite))
    suite.addTests(loader.loadTestsFromTestCase(TestAdversarialDeepDive))
    suite.addTests(loader.loadTestsFromTestCase(TestStatutoryFinancialStress))
    suite.addTests(loader.loadTestsFromTestCase(TestChallengerArtifactIntegrity))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*70)
    print("RUNNING CHALLENGER STRESS-TEST HARNESS (MATHEMATICAL ENGINES):")
    print("="*70)
    stress_tester = AdversarialStressTester()
    stress_results = stress_tester.run_all_tests()
    stress_success = stress_results.get("summary", {}).get("all_tests_passed", False)
    
    all_passed = result.wasSuccessful() and stress_success
    
    print("\n" + "="*70)
    print("MASTER ADVERSARIAL & STRESS VERIFICATION SUMMARY:")
    print(f"Unittest Suite Executed: {result.testsRun}")
    print(f"Unittest Successes:      {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Unittest Failures:       {len(result.failures)}")
    print(f"Unittest Errors:         {len(result.errors)}")
    print(f"Stress Tests Executed:   5")
    print(f"Stress Test Successes:   {5 if stress_success else 0}")
    print(f"Master Verdict:          {'PASS (APPROVE)' if all_passed else 'FAIL (REQUEST_CHANGES)'}")
    print("="*70)
    
    return all_passed

if __name__ == "__main__":
    success = run_master_suite()
    sys.exit(0 if success else 1)
