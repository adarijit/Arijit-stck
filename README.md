# Arijit-stck
All financial script

A comprehensive collection of financial calculation tools and utilities for personal finance, investment analysis, and business planning.

## 📋 Contents

### 🧮 Financial Calculator (`financial_calculator.py`)
A comprehensive financial calculator class that provides various financial calculation functions:

**Investment Calculations:**
- Compound Interest Calculator
- Simple Interest Calculator
- Present/Future Value Calculations
- Return on Investment (ROI) Analysis

**Loan & Credit Analysis:**
- EMI (Equated Monthly Installment) Calculator
- Loan Payment Analysis

**Portfolio Management:**
- Portfolio Performance Analysis
- Investment Breakdown and Weighting
- Gain/Loss Tracking

**Business Analysis:**
- Break-even Analysis
- Contribution Margin Calculations

### 📊 Practical Examples (`financial_examples.py`)
Real-world examples demonstrating practical applications:

- **Retirement Planning:** Calculate savings needed for retirement goals
- **Home Loan Comparison:** Compare different mortgage options
- **Investment Portfolio Tracking:** Analyze portfolio performance
- **Business Break-even Analysis:** Determine break-even points for businesses
- **Savings Goal Planning:** Plan monthly savings for various goals

### 🧪 Tests (`test_financial_calculator.py`)
Comprehensive test suite to validate all financial calculations and error handling.

## 🚀 Quick Start

### Run the Main Calculator Demo
```bash
python3 financial_calculator.py
```

### Explore Practical Examples
```bash
python3 financial_examples.py
```

### Run Tests
```bash
python3 test_financial_calculator.py
```

## 💡 Usage Examples

### Calculate Compound Interest
```python
from financial_calculator import FinancialCalculator

calc = FinancialCalculator()
result = calc.compound_interest(principal=10000, rate=0.08, time=5, compound_frequency=4)
print(f"Final Amount: ${result['final_amount']:,.2f}")
```

### Analyze Investment Portfolio
```python
portfolio = [
    {'name': 'Stock A', 'amount': 10000, 'current_value': 12000},
    {'name': 'Bond B', 'amount': 5000, 'current_value': 5200}
]
analysis = calc.portfolio_analysis(portfolio)
print(f"Portfolio ROI: {analysis['portfolio_roi_percentage']}%")
```

### Calculate Loan EMI
```python
emi_result = calc.loan_emi(principal=500000, rate=0.09, tenure=240)  # 20 years
print(f"Monthly EMI: ${emi_result['monthly_emi']:,.2f}")
```

## 🔧 Features

- **Comprehensive Calculations:** Wide range of financial formulas and calculations
- **Error Handling:** Robust input validation and error messages
- **Real-world Examples:** Practical scenarios for common financial decisions
- **Well-tested:** Complete test suite ensuring accuracy
- **Easy to Use:** Simple API with clear function signatures
- **Documentation:** Detailed docstrings and usage examples

## 📈 Supported Calculations

| Category | Functions |
|----------|-----------|
| **Interest** | Compound Interest, Simple Interest |
| **Loans** | EMI Calculator, Total Interest |
| **Investments** | ROI, Present/Future Value |
| **Portfolio** | Performance Analysis, Diversification |
| **Business** | Break-even Analysis, Profit Planning |

## 🎯 Use Cases

- **Personal Finance:** Retirement planning, savings goals, loan comparisons
- **Investment Analysis:** Portfolio tracking, ROI calculations
- **Business Planning:** Break-even analysis, profit projections
- **Education:** Learning financial concepts with practical examples
- **Financial Advisory:** Tools for financial advisors and consultants

## 🔒 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## 🤝 Contributing

Feel free to contribute by:
- Adding new financial calculations
- Improving existing functions
- Adding more practical examples
- Enhancing documentation
- Reporting bugs or suggesting features

## 📄 License

This project is licensed under the GPL v3 License - see the [LICENSE](LICENSE) file for details.

---

*Made with ❤️ for the financial community*