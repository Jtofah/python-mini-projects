# Doubling Penny Calculator

A simple Python program that demonstrates the incredible power of exponential growth through the classic "doubling penny" thought experiment.

## Why This Project Matters to Me

This simple calculator represents more than just math - it's about understanding the power of small, consistent actions. Just like a penny doubling each day becomes millions, the small efforts we make daily can compound into extraordinary results. Whether it's learning to code, building habits, or pursuing dreams, this project reminds me that starting small doesn't mean staying small.

## What It Does

The program calculates what happens when you start with a single penny and double it every day for a specified number of days. The results are truly mind-boggling:

- Day 1: $0.01
- Day 10: $5.12
- Day 20: $5,242.88
- Day 30: $10,737,418.24

## How It Works

The calculation follows the mathematical principle of exponential growth:
```
Value = Initial Amount × 2^(number of days)
```

Starting with $0.01 and doubling it n times gives us the final amount.

## Installation & Usage

### Prerequisites
- Python 3.x

### Running the Program

1. Clone this repository:
```bash
git clone https://github.com/yourusername/doubling-penny.git
cd doubling-penny
```

2. Run the program:
```bash
python doubling_penny.py
```

3. The program will output the total value after 30 days of doubling.

### Customizing the Days

To calculate for a different number of days, modify the function call in the code:
```python
value_after_days = double_penny(20)  # Change 20 to your desired number of days
```

## Example Output

```
The value after 30 days is $10737418.24
```

## The Math Behind It

This demonstrates **compound growth** - where growth builds upon previous growth. Each day, you're not just adding the same amount; you're doubling the entire accumulated value. This is the same principle behind:

- Compound interest in investments
- Viral growth on social media
- Learning and skill development
- Habit formation

## Key Takeaways

- **Small beginnings, massive results**: A penny becomes over $10 million in just 30 days
- **The power of consistency**: It's not about the size of the daily action, but the consistency
- **Exponential vs. linear thinking**: Our brains naturally think linearly, but compound effects are exponential
- **Patience pays off**: The biggest gains come in the later days

## Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses only built-in Python functions)

## Contributing

Feel free to fork this project and submit pull requests if you'd like to add features such as:
- Interactive input for custom day amounts
- Visualization of the growth curve
- Comparison with linear growth
- Different starting amounts


## Connect

If this project inspired you or taught you something new, I'd love to hear about it! Feel free to reach out or share your own "compound growth" stories.

---

*Remember: Every expert was once a beginner. Every pro was once an amateur. Every icon was once an unknown. The magic happens when small, consistent efforts compound over time.*