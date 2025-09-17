#!/usr/bin/env python3
"""
Test script for Financial Calculator
Simple tests to validate the financial calculations
"""

import sys
import os

# Add the current directory to Python path to import the financial calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from financial_calculator import FinancialCalculator


def test_compound_interest():
    """Test compound interest calculations."""
    calc = FinancialCalculator()
    
    # Test basic compound interest
    result = calc.compound_interest(1000, 0.05, 2, 1)
    expected_amount = 1000 * (1.05 ** 2)  # Should be 1102.50
    assert abs(result['final_amount'] - expected_amount) < 0.01, f"Expected {expected_amount}, got {result['final_amount']}"
    
    # Test with quarterly compounding
    result = calc.compound_interest(1000, 0.08, 1, 4)
    expected_amount = 1000 * (1 + 0.08/4) ** 4  # Should be approximately 1082.43
    assert abs(result['final_amount'] - expected_amount) < 0.01, f"Expected {expected_amount}, got {result['final_amount']}"
    
    print("✓ Compound interest tests passed")


def test_simple_interest():
    """Test simple interest calculations."""
    calc = FinancialCalculator()
    
    result = calc.simple_interest(1000, 0.05, 2)
    expected_interest = 1000 * 0.05 * 2  # Should be 100
    expected_amount = 1000 + expected_interest  # Should be 1100
    
    assert result['interest_earned'] == expected_interest, f"Expected {expected_interest}, got {result['interest_earned']}"
    assert result['final_amount'] == expected_amount, f"Expected {expected_amount}, got {result['final_amount']}"
    
    print("✓ Simple interest tests passed")


def test_loan_emi():
    """Test loan EMI calculations."""
    calc = FinancialCalculator()
    
    # Test with zero interest rate
    result = calc.loan_emi(12000, 0, 12)
    expected_emi = 12000 / 12  # Should be 1000
    assert result['monthly_emi'] == expected_emi, f"Expected {expected_emi}, got {result['monthly_emi']}"
    
    print("✓ Loan EMI tests passed")


def test_roi_calculation():
    """Test ROI calculations."""
    calc = FinancialCalculator()
    
    result = calc.roi_calculation(1000, 1200)
    expected_roi = ((1200 - 1000) / 1000) * 100  # Should be 20%
    
    assert result['roi_percentage'] == expected_roi, f"Expected {expected_roi}, got {result['roi_percentage']}"
    assert result['gain_loss'] == 200, f"Expected 200, got {result['gain_loss']}"
    
    print("✓ ROI calculation tests passed")


def test_present_future_value():
    """Test present and future value calculations."""
    calc = FinancialCalculator()
    
    # Test future value
    fv = calc.future_value(1000, 0.05, 2)
    expected_fv = 1000 * (1.05 ** 2)  # Should be 1102.50
    assert abs(fv - expected_fv) < 0.01, f"Expected {expected_fv}, got {fv}"
    
    # Test present value
    pv = calc.present_value(1102.50, 0.05, 2)
    expected_pv = 1102.50 / (1.05 ** 2)  # Should be 1000
    assert abs(pv - expected_pv) < 0.01, f"Expected {expected_pv}, got {pv}"
    
    print("✓ Present/Future value tests passed")


def test_portfolio_analysis():
    """Test portfolio analysis."""
    calc = FinancialCalculator()
    
    investments = [
        {'name': 'Stock A', 'amount': 1000, 'current_value': 1200},
        {'name': 'Stock B', 'amount': 2000, 'current_value': 1800}
    ]
    
    result = calc.portfolio_analysis(investments)
    
    assert result['total_invested'] == 3000, f"Expected 3000, got {result['total_invested']}"
    assert result['total_current_value'] == 3000, f"Expected 3000, got {result['total_current_value']}"
    assert result['total_gain_loss'] == 0, f"Expected 0, got {result['total_gain_loss']}"
    
    print("✓ Portfolio analysis tests passed")


def test_break_even_analysis():
    """Test break-even analysis."""
    calc = FinancialCalculator()
    
    result = calc.break_even_analysis(1000, 10, 20)
    expected_units = 1000 / (20 - 10)  # Should be 100
    expected_revenue = expected_units * 20  # Should be 2000
    
    assert result['break_even_units'] == expected_units, f"Expected {expected_units}, got {result['break_even_units']}"
    assert result['break_even_revenue'] == expected_revenue, f"Expected {expected_revenue}, got {result['break_even_revenue']}"
    
    print("✓ Break-even analysis tests passed")


def test_error_handling():
    """Test error handling for invalid inputs."""
    calc = FinancialCalculator()
    
    try:
        calc.compound_interest(-1000, 0.05, 2)  # Negative principal
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        calc.loan_emi(1000, 0.05, 0)  # Zero tenure
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        calc.break_even_analysis(1000, 20, 15)  # Selling price less than variable cost
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("✓ Error handling tests passed")


def run_all_tests():
    """Run all tests."""
    print("Running Financial Calculator Tests...\n")
    
    test_compound_interest()
    test_simple_interest()
    test_loan_emi()
    test_roi_calculation()
    test_present_future_value()
    test_portfolio_analysis()
    test_break_even_analysis()
    test_error_handling()
    
    print("\n🎉 All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()