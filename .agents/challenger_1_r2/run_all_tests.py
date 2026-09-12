import sys, unittest
sys.stdout.reconfigure(encoding='utf-8')

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('d:/promotion/.agents/challenger_1_r2', pattern='test_scenario*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    print('='*60)
    print(f'Total tests run: {result.testsRun}')
    print(f'Failures: {len(result.failures)}')
    print(f'Errors: {len(result.errors)}')
    if result.failures:
        print('\n--- FAILURES ---')
        for test, trace in result.failures:
            print(f'Test: {test}')
            print(trace)
    if result.errors:
        print('\n--- ERRORS ---')
        for test, trace in result.errors:
            print(f'Test: {test}')
            print(trace)
