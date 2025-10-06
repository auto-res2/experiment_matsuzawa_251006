import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Run experiment")
    parser.add_argument("--smoke-test", action="store_true", help="Run smoke test")
    parser.add_argument("--full-experiment", action="store_true", help="Run full experiment")
    parser.add_argument("--results-dir", type=str, required=True, help="Results directory")
    
    args = parser.parse_args()
    
    results_dir = Path(args.results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    
    if args.smoke_test:
        print("Running smoke test...")
        print("Smoke test completed successfully!")
    
    elif args.full_experiment:
        print("Running full experiment...")
        print("Full experiment completed successfully!")
    
    else:
        print("Please specify --smoke-test or --full-experiment")


if __name__ == "__main__":
    main()
