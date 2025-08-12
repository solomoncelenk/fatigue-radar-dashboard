"""Perceived Value Multiplier (PVM) calculator and anchor recommendation."""


def get_score(name: str) -> float:
    """Prompt for a score between 1 and 10 and return it as a float."""
    while True:
        try:
            value = float(input(f"Enter {name} score (1-10): "))
            if 1 <= value <= 10:
                return value
            print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_pvm(vd: float, cb: float, cs: float) -> float:
    """Calculate the PVM score from the given metrics."""
    return ((vd * 0.4) + (cb * 0.3) + ((10 - cs) * 0.3)) / 10


def recommend_anchor(pvm: float) -> str:
    """Return the anchoring recommendation for the given PVM score."""
    if pvm >= 0.85:
        return "Anchor at high end of your target range."
    if pvm >= 0.70:
        return "Anchor in mid-high range; keep room for concessions."
    return "Anchor conservatively and build value drivers before pushing price."


def main() -> None:
    vd = get_score("Value Drivers (VD)")
    cb = get_score("Competitive Benchmark (CB)")
    cs = get_score("Cost Structure (CS)")
    pvm = calculate_pvm(vd, cb, cs)
    print(f"PVM Score: {pvm:.2f}")
    print("Recommendation:", recommend_anchor(pvm))


if __name__ == "__main__":
    main()
