#!/usr/bin/env python3
"""
Financial Calculator Examples
Real-world examples of using the financial calculator for common scenarios
"""

from financial_calculator import FinancialCalculator


def retirement_planning_example():
    """Example: Retirement planning with compound interest."""
    print("🎯 RETIREMENT PLANNING EXAMPLE")
    print("=" * 50)
    
    calc = FinancialCalculator()
    
    # Scenario: 25-year-old wants to retire at 65 with $1M
    current_age = 25
    retirement_age = 65
    years_to_retirement = retirement_age - current_age
    target_amount = 1000000
    expected_return = 0.07  # 7% annual return
    
    # Calculate required monthly investment
    print(f"Age: {current_age}, Retirement age: {retirement_age}")
    print(f"Years to retirement: {years_to_retirement}")
    print(f"Target retirement amount: ${target_amount:,.2f}")
    print(f"Expected annual return: {expected_return*100}%\n")
    
    # Calculate present value of target amount
    present_value_needed = calc.present_value(target_amount, expected_return, years_to_retirement)
    print(f"Present value of ${target_amount:,.2f} in {years_to_retirement} years: ${present_value_needed:,.2f}")
    
    # Show different investment scenarios
    monthly_investments = [500, 1000, 1500, 2000]
    
    print(f"\nMonthly Investment Scenarios:")
    print("-" * 40)
    
    for monthly_amount in monthly_investments:
        annual_investment = monthly_amount * 12
        result = calc.compound_interest(annual_investment, expected_return, years_to_retirement, 1)
        
        # For annuity (monthly contributions), we need to calculate future value of annuity
        # FV = PMT × [((1 + r)^n - 1) / r]
        monthly_rate = expected_return / 12
        months = years_to_retirement * 12
        if monthly_rate > 0:
            fv_annuity = monthly_amount * (((1 + monthly_rate) ** months - 1) / monthly_rate)
        else:
            fv_annuity = monthly_amount * months
        
        print(f"${monthly_amount:>4}/month → Final amount: ${fv_annuity:>12,.2f}")
        if fv_annuity >= target_amount:
            print(f"                   ✅ Meets retirement goal!")
        else:
            shortfall = target_amount - fv_annuity
            print(f"                   ❌ Shortfall: ${shortfall:,.2f}")
    
    print("\n")


def home_loan_comparison():
    """Example: Comparing different home loan options."""
    print("🏠 HOME LOAN COMPARISON")
    print("=" * 50)
    
    calc = FinancialCalculator()
    
    loan_amount = 400000  # $400k home loan
    
    # Different loan scenarios
    scenarios = [
        {"name": "30-year fixed", "rate": 0.065, "years": 30},
        {"name": "15-year fixed", "rate": 0.055, "years": 15},
        {"name": "20-year fixed", "rate": 0.060, "years": 20},
    ]
    
    print(f"Loan Amount: ${loan_amount:,.2f}\n")
    
    for scenario in scenarios:
        tenure_months = scenario["years"] * 12
        result = calc.loan_emi(loan_amount, scenario["rate"], tenure_months)
        
        print(f"{scenario['name']} ({scenario['rate']*100:.1f}% APR):")
        print(f"  Monthly EMI: ${result['monthly_emi']:>10,.2f}")
        print(f"  Total Payment: ${result['total_payment']:>8,.2f}")
        print(f"  Total Interest: ${result['total_interest']:>7,.2f}")
        print(f"  Interest as % of loan: {(result['total_interest']/loan_amount)*100:>5.1f}%")
        print()


def investment_portfolio_tracking():
    """Example: Track and analyze investment portfolio performance."""
    print("📈 INVESTMENT PORTFOLIO ANALYSIS")
    print("=" * 50)
    
    calc = FinancialCalculator()
    
    # Sample portfolio
    portfolio = [
        {'name': 'S&P 500 ETF', 'amount': 25000, 'current_value': 28500},
        {'name': 'Tech Stocks', 'amount': 15000, 'current_value': 18200},
        {'name': 'Real Estate REIT', 'amount': 10000, 'current_value': 10800},
        {'name': 'Bonds', 'amount': 8000, 'current_value': 8200},
        {'name': 'International ETF', 'amount': 12000, 'current_value': 11400},
    ]
    
    analysis = calc.portfolio_analysis(portfolio)
    
    print(f"Portfolio Summary:")
    print(f"Total Invested: ${analysis['total_invested']:>12,.2f}")
    print(f"Current Value: ${analysis['total_current_value']:>13,.2f}")
    print(f"Total Gain/Loss: ${analysis['total_gain_loss']:>11,.2f}")
    print(f"Portfolio ROI: {analysis['portfolio_roi_percentage']:>14.2f}%")
    print(f"Number of Holdings: {analysis['number_of_investments']:>9}")
    
    print(f"\nDetailed Breakdown:")
    print("-" * 70)
    print(f"{'Investment':<18} {'Invested':<10} {'Current':<10} {'Gain/Loss':<10} {'ROI%':<8} {'Weight%':<8}")
    print("-" * 70)
    
    for inv in analysis['investments']:
        print(f"{inv['name']:<18} ${inv['invested']:>8,.0f} ${inv['current_value']:>8,.0f} "
              f"${inv['gain_loss']:>8,.0f} {inv['roi_percentage']:>6.1f}% {inv['portfolio_weight']:>6.1f}%")
    
    print("\n")


def business_break_even_analysis():
    """Example: Business break-even analysis for a startup."""
    print("💼 BUSINESS BREAK-EVEN ANALYSIS")
    print("=" * 50)
    
    calc = FinancialCalculator()
    
    # Startup café example
    print("Scenario: Opening a small café")
    print("-" * 30)
    
    fixed_costs = 8000  # Monthly rent, salaries, insurance, etc.
    variable_cost_per_cup = 2.50  # Cost of coffee, milk, cup, etc.
    selling_price_per_cup = 5.00  # Selling price
    
    result = calc.break_even_analysis(fixed_costs, variable_cost_per_cup, selling_price_per_cup)
    
    print(f"Fixed Costs (monthly): ${result['fixed_costs']:,.2f}")
    print(f"Variable Cost per cup: ${result['variable_cost_per_unit']:.2f}")
    print(f"Selling Price per cup: ${result['selling_price_per_unit']:.2f}")
    print(f"Contribution Margin: ${result['contribution_margin']:.2f}")
    print()
    print(f"Break-even Analysis:")
    print(f"  Units to break-even: {result['break_even_units']:>8,.0f} cups/month")
    print(f"  Revenue to break-even: ${result['break_even_revenue']:>6,.2f}/month")
    print(f"  Daily cups needed: {result['break_even_units']/30:>12,.0f} cups/day")
    
    # Show profit scenarios
    print(f"\nProfit Scenarios:")
    print("-" * 25)
    cups_per_day = [100, 150, 200, 250, 300]
    
    for daily_cups in cups_per_day:
        monthly_cups = daily_cups * 30
        monthly_revenue = monthly_cups * selling_price_per_cup
        monthly_variable_costs = monthly_cups * variable_cost_per_cup
        monthly_profit = monthly_revenue - monthly_variable_costs - fixed_costs
        
        print(f"{daily_cups:>3} cups/day → Monthly profit: ${monthly_profit:>7,.2f}")
    
    print("\n")


def savings_goal_planning():
    """Example: Planning to save for different goals."""
    print("💰 SAVINGS GOAL PLANNING")
    print("=" * 50)
    
    calc = FinancialCalculator()
    
    goals = [
        {"name": "Emergency Fund", "target": 15000, "timeline": 2, "rate": 0.02},
        {"name": "New Car", "target": 30000, "timeline": 3, "rate": 0.04},
        {"name": "House Down Payment", "target": 80000, "timeline": 5, "rate": 0.06},
        {"name": "Vacation", "target": 8000, "timeline": 1, "rate": 0.01},
    ]
    
    print("Savings Goals Analysis:")
    print("-" * 60)
    print(f"{'Goal':<20} {'Target':<10} {'Years':<6} {'Rate':<6} {'Monthly Savings'}")
    print("-" * 60)
    
    for goal in goals:
        # Calculate required present value
        pv_needed = calc.present_value(goal["target"], goal["rate"], goal["timeline"])
        
        # For monthly savings, we calculate the payment needed for an annuity
        monthly_rate = goal["rate"] / 12
        months = goal["timeline"] * 12
        
        if monthly_rate > 0:
            # PMT = FV × r / ((1 + r)^n - 1)
            monthly_payment = goal["target"] * monthly_rate / ((1 + monthly_rate) ** months - 1)
        else:
            monthly_payment = goal["target"] / months
        
        print(f"{goal['name']:<20} ${goal['target']:>8,.0f} {goal['timeline']:>4}y {goal['rate']*100:>4.0f}% "
              f"${monthly_payment:>12,.2f}")
    
    print("\n")


def main():
    """Run all examples."""
    print("🔢 FINANCIAL CALCULATOR - PRACTICAL EXAMPLES")
    print("=" * 60)
    print()
    
    retirement_planning_example()
    home_loan_comparison()
    investment_portfolio_tracking()
    business_break_even_analysis()
    savings_goal_planning()
    
    print("💡 These examples demonstrate practical applications of financial calculations")
    print("   for personal finance, investments, business planning, and goal setting.")


if __name__ == "__main__":
    main()