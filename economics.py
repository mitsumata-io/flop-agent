"""Offline FLOP scenario economics; no credentials, network, or allocation claims."""
import argparse
from decimal import Decimal, InvalidOperation
import json

def number(value, name, upper=None):
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(name + " must be a finite nonnegative number")
    if not result.is_finite() or result < 0 or (upper is not None and result > upper):
        raise ValueError(name + " is outside its allowed range")
    return result

def scenario(cash_cost=0, hours=0, hourly_cost=0, tokens=0,
             liquid_fraction=0, realization_probability=0, token_price=None):
    """Probability is joint realization of the supplied allocation, liquidity, and price."""
    cash = number(cash_cost, "cash_cost")
    time = number(hours, "hours")
    rate = number(hourly_cost, "hourly_cost")
    amount = number(tokens, "tokens")
    liquid = number(liquid_fraction, "liquid_fraction", Decimal(1))
    probability = number(realization_probability, "realization_probability", Decimal(1))
    price = None if token_price is None else number(token_price, "token_price")
    cost = cash + time * rate
    realized = amount * liquid * probability
    revenue = None if price is None else realized * price
    return {
        "classification": "hypothetical_scenario_not_allocation_or_forecast",
        "total_cost": str(cost),
        "probability_weighted_liquid_tokens": str(realized),
        "break_even_token_price": None if realized == 0 else str(cost / realized),
        "scenario_net_profit": None if revenue is None else str(revenue - cost),
        "zero_reward_net_profit": str(-cost),
        "allocation_verified_by_this_tool": False,
        "limitations": "All inputs are supplied assumptions. No eligibility, token price, unlock rule, independence, taxes, or market liquidity is inferred.",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("cash-cost", "hours", "hourly-cost", "tokens", "liquid-fraction", "realization-probability"):
        parser.add_argument("--" + name, default="0")
    parser.add_argument("--token-price")
    args = vars(parser.parse_args())
    try:
        print(json.dumps(scenario(**args), indent=2))
    except ValueError as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()
