#!/usr/bin/env python3
"""
Financial Calculator Script
A comprehensive financial calculator with various financial functions

Author: Arijit
Description: Collection of financial calculations for investments, loans, and portfolio analysis
"""

import math
from typing import List, Dict, Union, Tuple


class FinancialCalculator:
    """A comprehensive financial calculator class."""
    
    def __init__(self):
        """Initialize the Financial Calculator."""
        pass
    
    def compound_interest(self, principal: float, rate: float, time: float, 
                         compound_frequency: int = 1) -> Dict[str, float]:
        """
        Calculate compound interest.
        
        Args:
            principal: Initial investment amount
            rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
            time: Time in years
            compound_frequency: Number of times interest compounds per year
            
        Returns:
            Dictionary with final amount, interest earned, and effective rate
        """
        if principal <= 0 or rate < 0 or time < 0:
            raise ValueError("Principal must be positive, rate and time must be non-negative")
        
        final_amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
        interest_earned = final_amount - principal
        effective_rate = (final_amount / principal) ** (1 / time) - 1 if time > 0 else 0
        
        return {
            'principal': principal,
            'final_amount': round(final_amount, 2),
            'interest_earned': round(interest_earned, 2),
            'effective_annual_rate': round(effective_rate * 100, 2)
        }
    
    def simple_interest(self, principal: float, rate: float, time: float) -> Dict[str, float]:
        """
        Calculate simple interest.
        
        Args:
            principal: Initial amount
            rate: Annual interest rate (as decimal)
            time: Time in years
            
        Returns:
            Dictionary with final amount and interest earned
        """
        if principal <= 0 or rate < 0 or time < 0:
            raise ValueError("Principal must be positive, rate and time must be non-negative")
        
        interest = principal * rate * time
        final_amount = principal + interest
        
        return {
            'principal': principal,
            'interest_earned': round(interest, 2),
            'final_amount': round(final_amount, 2)
        }
    
    def loan_emi(self, principal: float, rate: float, tenure: int) -> Dict[str, float]:
        """
        Calculate Equated Monthly Installment (EMI) for a loan.
        
        Args:
            principal: Loan amount
            rate: Annual interest rate (as decimal)
            tenure: Loan tenure in months
            
        Returns:
            Dictionary with EMI, total payment, and total interest
        """
        if principal <= 0 or rate < 0 or tenure <= 0:
            raise ValueError("Principal must be positive, rate must be non-negative, tenure must be positive")
        
        monthly_rate = rate / 12
        if monthly_rate == 0:
            emi = principal / tenure
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** tenure / ((1 + monthly_rate) ** tenure - 1)
        
        total_payment = emi * tenure
        total_interest = total_payment - principal
        
        return {
            'loan_amount': principal,
            'monthly_emi': round(emi, 2),
            'total_payment': round(total_payment, 2),
            'total_interest': round(total_interest, 2),
            'tenure_months': tenure
        }
    
    def roi_calculation(self, initial_investment: float, final_value: float, 
                       time_period: float = None) -> Dict[str, float]:
        """
        Calculate Return on Investment (ROI).
        
        Args:
            initial_investment: Initial investment amount
            final_value: Final value of investment
            time_period: Time period in years (optional)
            
        Returns:
            Dictionary with ROI percentage and annualized ROI if time_period provided
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive")
        
        roi = (final_value - initial_investment) / initial_investment * 100
        
        result = {
            'initial_investment': initial_investment,
            'final_value': final_value,
            'roi_percentage': round(roi, 2),
            'gain_loss': round(final_value - initial_investment, 2)
        }
        
        if time_period and time_period > 0:
            annualized_roi = ((final_value / initial_investment) ** (1 / time_period) - 1) * 100
            result['annualized_roi_percentage'] = round(annualized_roi, 2)
            result['time_period_years'] = time_period
        
        return result
    
    def present_value(self, future_value: float, rate: float, time: float) -> float:
        """
        Calculate present value of future cash flow.
        
        Args:
            future_value: Future value of money
            rate: Discount rate (as decimal)
            time: Time period in years
            
        Returns:
            Present value
        """
        if rate < 0 or time < 0:
            raise ValueError("Rate and time must be non-negative")
        
        if rate == 0:
            return future_value
        
        pv = future_value / (1 + rate) ** time
        return round(pv, 2)
    
    def future_value(self, present_value: float, rate: float, time: float) -> float:
        """
        Calculate future value of present cash flow.
        
        Args:
            present_value: Present value of money
            rate: Interest rate (as decimal)
            time: Time period in years
            
        Returns:
            Future value
        """
        if rate < 0 or time < 0:
            raise ValueError("Rate and time must be non-negative")
        
        fv = present_value * (1 + rate) ** time
        return round(fv, 2)
    
    def portfolio_analysis(self, investments: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[float, List]]:
        """
        Analyze a portfolio of investments.
        
        Args:
            investments: List of dictionaries with investment details
                        Each dict should have: 'name', 'amount', 'current_value'
                        
        Returns:
            Dictionary with portfolio analysis
        """
        if not investments:
            raise ValueError("Investments list cannot be empty")
        
        total_invested = sum(inv['amount'] for inv in investments)
        total_current_value = sum(inv['current_value'] for inv in investments)
        total_gain_loss = total_current_value - total_invested
        portfolio_roi = (total_gain_loss / total_invested) * 100 if total_invested > 0 else 0
        
        investment_breakdown = []
        for inv in investments:
            gain_loss = inv['current_value'] - inv['amount']
            roi = (gain_loss / inv['amount']) * 100 if inv['amount'] > 0 else 0
            weight = (inv['current_value'] / total_current_value) * 100 if total_current_value > 0 else 0
            
            investment_breakdown.append({
                'name': inv['name'],
                'invested': inv['amount'],
                'current_value': inv['current_value'],
                'gain_loss': round(gain_loss, 2),
                'roi_percentage': round(roi, 2),
                'portfolio_weight': round(weight, 2)
            })
        
        return {
            'total_invested': round(total_invested, 2),
            'total_current_value': round(total_current_value, 2),
            'total_gain_loss': round(total_gain_loss, 2),
            'portfolio_roi_percentage': round(portfolio_roi, 2),
            'number_of_investments': len(investments),
            'investments': investment_breakdown
        }
    
    def break_even_analysis(self, fixed_costs: float, variable_cost_per_unit: float, 
                           selling_price_per_unit: float) -> Dict[str, float]:
        """
        Calculate break-even point for a business.
        
        Args:
            fixed_costs: Total fixed costs
            variable_cost_per_unit: Variable cost per unit
            selling_price_per_unit: Selling price per unit
            
        Returns:
            Dictionary with break-even analysis
        """
        if selling_price_per_unit <= variable_cost_per_unit:
            raise ValueError("Selling price must be greater than variable cost per unit")
        
        contribution_margin = selling_price_per_unit - variable_cost_per_unit
        break_even_units = fixed_costs / contribution_margin
        break_even_revenue = break_even_units * selling_price_per_unit
        
        return {
            'fixed_costs': fixed_costs,
            'variable_cost_per_unit': variable_cost_per_unit,
            'selling_price_per_unit': selling_price_per_unit,
            'contribution_margin': round(contribution_margin, 2),
            'break_even_units': round(break_even_units, 2),
            'break_even_revenue': round(break_even_revenue, 2)
        }


def main():
    """Main function to demonstrate the financial calculator."""
    calc = FinancialCalculator()
    
    print("=== Financial Calculator Demo ===\n")
    
    # Compound Interest Example
    print("1. Compound Interest Calculation:")
    ci_result = calc.compound_interest(10000, 0.08, 5, 4)
    print(f"   Investment of ${ci_result['principal']:,.2f} at 8% annually for 5 years")
    print(f"   Final Amount: ${ci_result['final_amount']:,.2f}")
    print(f"   Interest Earned: ${ci_result['interest_earned']:,.2f}")
    print(f"   Effective Annual Rate: {ci_result['effective_annual_rate']}%\n")
    
    # Loan EMI Example
    print("2. Loan EMI Calculation:")
    emi_result = calc.loan_emi(500000, 0.09, 240)  # 20 years
    print(f"   Loan Amount: ${emi_result['loan_amount']:,.2f}")
    print(f"   Monthly EMI: ${emi_result['monthly_emi']:,.2f}")
    print(f"   Total Payment: ${emi_result['total_payment']:,.2f}")
    print(f"   Total Interest: ${emi_result['total_interest']:,.2f}\n")
    
    # ROI Example
    print("3. ROI Calculation:")
    roi_result = calc.roi_calculation(15000, 22000, 3)
    print(f"   Initial Investment: ${roi_result['initial_investment']:,.2f}")
    print(f"   Final Value: ${roi_result['final_value']:,.2f}")
    print(f"   ROI: {roi_result['roi_percentage']}%")
    print(f"   Annualized ROI: {roi_result['annualized_roi_percentage']}%\n")
    
    # Portfolio Analysis Example
    print("4. Portfolio Analysis:")
    sample_portfolio = [
        {'name': 'Stock A', 'amount': 10000, 'current_value': 12000},
        {'name': 'Stock B', 'amount': 15000, 'current_value': 14000},
        {'name': 'Bond C', 'amount': 5000, 'current_value': 5200}
    ]
    portfolio_result = calc.portfolio_analysis(sample_portfolio)
    print(f"   Total Invested: ${portfolio_result['total_invested']:,.2f}")
    print(f"   Current Value: ${portfolio_result['total_current_value']:,.2f}")
    print(f"   Total Gain/Loss: ${portfolio_result['total_gain_loss']:,.2f}")
    print(f"   Portfolio ROI: {portfolio_result['portfolio_roi_percentage']}%\n")
    
    # Break-even Analysis Example
    print("5. Break-even Analysis:")
    be_result = calc.break_even_analysis(50000, 20, 35)
    print(f"   Fixed Costs: ${be_result['fixed_costs']:,.2f}")
    print(f"   Break-even Units: {be_result['break_even_units']:,.2f}")
    print(f"   Break-even Revenue: ${be_result['break_even_revenue']:,.2f}")


if __name__ == "__main__":
    main()