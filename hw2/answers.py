r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 2 answers


def part2_overfit_hp():
    wstd, lr, reg = 0, 0, 0
    # ====== YOUR CODE: ======
    wstd = 0.1
    lr = 0.02
    # ========================
    return dict(wstd=wstd, lr=lr, reg=reg)


def part2_optim_hp():
    wstd, lr_vanilla, lr_momentum, lr_rmsprop, reg, = 0, 0, 0, 0, 0

    # You may want to use different learning rates for each optimizer.
    # ====== YOUR CODE: ======
    wstd = 0.1
    lr_vanilla = 0.04
    lr_momentum = 0.003
    lr_rmsprop = 8e-5
    reg = 0.01
    # ========================
    return dict(wstd=wstd, lr_vanilla=lr_vanilla, lr_momentum=lr_momentum,
                lr_rmsprop=lr_rmsprop, reg=reg)


def part2_dropout_hp():
    wstd, lr, = 0, 0
    # dropout.
    # ====== YOUR CODE: ======
    wstd = 1
    lr = 0.0001
    # ========================
    return dict(wstd=wstd, lr=lr)


part2_q1 = r"""
**Your answer:**
1.  As seen in the graphs of the three dropout's configurations, the no-dropout model does overfit the data noticeably.  
    We get a train accuracy of about 50%, but the test accuracy is around 20%.  
    On the other hand, when we do use dropout we don't see any major overfitting (24 vs. 24 and 13 vs. 16).  
2.  When using the low dropout setting the model at least somewhat manages to learn (gets around 25% accuracy),  
    compared to the higher dropout setting that gets stuck at the naive, random guess, 10% area.  
"""

part2_q2 = r"""
**Your answer:**  
This scenario is possible if the two following phenomenons starts to happen:
1.  Some edge cases samples are starting to be classified correctly, which would increase the accuracy of the test  
    (while not decreasing the loss that much).
2.  Some more obvious cases samples that weren't classified correctly still aren't, but their predictions gets farther away  
    from the ideal score (one-hot vector), which wouldn't decrease the accuracy but increase the loss.  
Given both phenomenons are happening together, on average over the test data, we should see an increase in both accuracy and loss.
"""
# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""


part3_q4 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""
# ==============
