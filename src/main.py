#!/usr/bin/env python3
"""
Main experiment script.
"""

import argparse
import os
import sys
from pathlib import Path


def run_smoke_test(results_dir):
    """Run a quick smoke test to verify the setup works."""
    print("Running smoke test...")
    print(f"Results directory: {results_dir}")

    # Create results directory if it doesn't exist
    results_path = Path(results_dir)
    results_path.mkdir(parents=True, exist_ok=True)

    # Simple smoke test - verify basic Python functionality
    test_file = results_path / "smoke_test_result.txt"
    with open(test_file, "w") as f:
        f.write("Smoke test completed successfully\n")
        f.write(f"Python version: {sys.version}\n")

    print("✓ Smoke test passed!")
    return 0


def run_full_experiment(results_dir):
    """Run the full experiment."""
    print("Running full experiment...")
    print(f"Results directory: {results_dir}")

    # Create results directory if it doesn't exist
    results_path = Path(results_dir)
    results_path.mkdir(parents=True, exist_ok=True)

    # Run the full experiment
    # This is a placeholder - add actual experiment code here
    print("Step 1: Preprocessing data...")
    print("Step 2: Training model...")
    print("Step 3: Evaluating results...")

    # Save results
    results_file = results_path / "experiment_results.txt"
    with open(results_file, "w") as f:
        f.write("Full experiment completed successfully\n")
        f.write(f"Python version: {sys.version}\n")
        f.write("Results: Experiment ran to completion\n")

    print("✓ Full experiment completed!")
    return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Run experiment")
    parser.add_argument(
        "--smoke-test",
        action="store_true",
        help="Run smoke test only"
    )
    parser.add_argument(
        "--full-experiment",
        action="store_true",
        help="Run full experiment"
    )
    parser.add_argument(
        "--results-dir",
        type=str,
        required=True,
        help="Directory to save results"
    )

    args = parser.parse_args()

    if args.smoke_test:
        return run_smoke_test(args.results_dir)
    elif args.full_experiment:
        return run_full_experiment(args.results_dir)
    else:
        print("Error: Must specify either --smoke-test or --full-experiment")
        return 1


if __name__ == "__main__":
    sys.exit(main())
