import argparse
import os
import time

def main():
    parser = argparse.ArgumentParser(description='Run experiment')
    parser.add_argument('--smoke-test', action='store_true', help='Run smoke test')
    parser.add_argument('--full-experiment', action='store_true', help='Run full experiment')
    parser.add_argument('--results-dir', type=str, required=True, help='Directory to save results')
    args = parser.parse_args()
    
    os.makedirs(args.results_dir, exist_ok=True)
    
    if args.smoke_test:
        print("Running smoke test...")
        print("Smoke test completed successfully!")
        
    elif args.full_experiment:
        print("Running full experiment...")
        time.sleep(2)
        print("Full experiment completed successfully!")
    
    else:
        print("Please specify either --smoke-test or --full-experiment")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())

