---
sidebar_position: 1
sidebar_label: Practical Guide 1
sidebar_class_name: green
sidebar_key: unique-sidebar-item-key
---

# Let's build our first agent

### Dependencies

- Python 3.12
- uv - package management tool
- [Groq](https://console.groq.com/) - LLM provider.

### Sanity Check on accessing Groq

```python
from langchain_groq import ChatGroq
GROQ_API_KEY = os.getenv("GROQ_API_KEY") # Add it from the environment variable in an env file

GROQ_MODEL_NAME = "openai/gpt-oss-120b"

chat_groq = ChatGroq(
    model_name=GROQ_MODEL_NAME,
    api_key=GROQ_API_KEY,
)

response = await chat_groq.ainvoke("what is an AI Agent? Explain in a simple sentence.")
print(response.content)

```

:::note[Task]

**Create an AI Agent which will be capable of generating python code for given user input**

:::

### Step 1: Define your prompt

```python
prompt = """
You are AI Agent capable of generating code for the give input.

Instructions:
1. Generate code in Python language.
2. Do not install any libraries, assume all libraries are already installed.

Input: {user_input}
"""
```

### Step 2: Access Groq and get responses

```python
user_input = "Write a python function which plots a sine wave with some sample data points."

prompt_to_llm = prompt.format(user_input=user_input)

response = await chat_groq.ainvoke(prompt_to_llm)
print(response.content)
```

#### Observe the response provided from the model

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(
    start: float = 0.0,
    stop: float = 2 * np.pi,
    num_samples: int = 500,
    num_points: int = 12,
    amplitude: float = 1.0,
    frequency: float = 1.0,
    phase: float = 0.0,
    line_kwargs: dict = None,
    point_kwargs: dict = None,
) -> None:
    """
    Plot a sine wave together with a few sample data points.

    Parameters
    ----------
    start, stop : float
        Range of the x‑axis (in radians). Default is one full period (0 → 2π).
    num_samples : int
        Number of points used to draw the smooth sine curve.
    num_points : int
        Number of discrete sample points that will be over‑laid on the curve.
    amplitude, frequency, phase : float
        Standard sine‑wave parameters: y = A·sin(2π·f·x + φ).
    line_kwargs, point_kwargs : dict or None
        Additional keyword arguments passed to ``plt.plot`` (for the line)
        and ``plt.scatter`` (for the sample points).  If ``None`` sensible
        defaults are used.

    Returns
    -------
    None
        The function displays the plot using ``plt.show()``.
    """
    # ------------------------------------------------------------------
    # 1. Prepare the smooth curve
    # ------------------------------------------------------------------
    x_smooth = np.linspace(start, stop, num_samples)
    y_smooth = amplitude * np.sin(2 * np.pi * frequency * x_smooth + phase)

    # ------------------------------------------------------------------
    # 2. Choose sample locations (equally spaced in the same interval)
    # ------------------------------------------------------------------
    x_samples = np.linspace(start, stop, num_points)
    y_samples = amplitude * np.sin(2 * np.pi * frequency * x_samples + phase)

    # ------------------------------------------------------------------
    # 3. Plotting
    # ------------------------------------------------------------------
    if line_kwargs is None:
        line_kwargs = {"color": "steelblue", "linewidth": 2, "label": "Sine wave"}
    if point_kwargs is None:
        point_kwargs = {
            "color": "orange",
            "edgecolor": "k",
            "s": 80,
            "zorder": 5,
            "label": f"{num_points} sample points",
        }

    plt.figure(figsize=(8, 4))
    plt.plot(x_smooth, y_smooth, **line_kwargs)
    plt.scatter(x_samples, y_samples, **point_kwargs)

    # ------------------------------------------------------------------
    # 4. Cosmetic tweaks
    # ------------------------------------------------------------------
    plt.title("Sine Wave with Sample Data Points")
    plt.xlabel("x (radians)")
    plt.ylabel("y")
    plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Plot a standard sine wave (amplitude=1, frequency=1) with 8 sample points
    plot_sine_wave(num_points=8)

**Explanation of the key parts**

| Section            | What it does                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| Imports            | `numpy` for numeric work, `matplotlib.pyplot` for plotting.                                                   |
| Function signature | Allows flexible control over the wave parameters, number of smooth points, and number of highlighted samples. |
| Curve generation   | `x_smooth`/`y_smooth` give a dense line for a clean-looking wave.                                             |
| Sample points      | `x_samples`/`y_samples` are a smaller set of points that are plotted with `scatter`.                          |
| Default styling    | Reasonable colours and sizes are provided, but callers can override them via `line_kwargs` / `point_kwargs`.  |
| Plot cosmetics     | Title, axis labels, grid, legend, and `tight_layout` for a tidy figure.                                       |
| Example block      | When the script is run directly, it calls the function with a simple configuration.                           |

Running the script will open a window (or inline cell, if used in a Jupyter notebook) displaying the sine wave together with the chosen sample data points. No external libraries need to be installed beyond the standard `numpy` and `matplotlib`, which are assumed to be available.

```
