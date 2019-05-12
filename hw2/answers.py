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
1. It seems that more depth tends to produce better results until a certain point,  
after which more depth tends to make the results significantly worse.  
A depth of L=4 + Linear_layers=3 = 7 for K=[32] produced the best results,  
while a depth of L=2 + Linear_layers=3 = 5 for K=[64] produced the best results.  
This is probably due to each being complex enough to learn the problem,  
but not so complex that it suffers from overfitting vanishing gradients.  
2. For L=16 the network was not trainable, as we can see it produced no improvement from the start and stopped due to early stopping.  
This is probably due to vanishing gradients, as with a network that is too long the gradients tend to get smaller as  
they get deeper into the start, due to the multiplicative nature of the chain rule.  
Possible solutions for this problem are the use of skip connections (such as those used in residual networks i.e ResNet)  
and batch normalization.

"""

part3_q2 = r"""
It seems that like more depth, more filters tend to produce better results until a certain point,  
with K = [258] and L=4 doing the best, probably due to providing enough parameters without overfitting.  
This makes sense, as using too many parameters means that we are using a model too complex for our problem.  
With too much depth we can see that the same problem of vanishing gradients we observed previously happens with K=[128],  
and in general moving from L=4 to L=8 saw significantly worse results, probably due to this problem and overfitting.  
We can see that adding more filters tends to produce better results than more depth,  
which, as we saw in part 1.1, only works up to a certain point and to lower precision.  
Although not enough depth and too many features can cause problems, as we see in L=2 and K=[258]

"""

part3_q3 = r"""
We see in the results for these experiments that the best results were produced with L=2,  
probably due to the fact that K=[64, 128, 256] provided us enough parameters for the learning process,  
and any more depth probably resulted in more overfitting and vanishing gradients, as is evidenced by the early stopping  
for L=3 and L=4. 

"""


part3_q4 = r"""
1. In order to combat the problem of vanishing gradients, we added skip connection and batch normalization to the feature extractor,  
and dropout to the classifer.  
This was done to provide more regularization and to make sure the gradients don't vanish.  
We decided to make every convolution layer a skip connection and use batch normalization before each one.  
We also used dropout before every Linear layer.  
  
2. we can see that our network produced significantly better results than those in experiment 1.3  
(which is the best point of comparison due to having similar parameters) and that we did not suffer from vanishing gradients.  
We still suffered from overfitting (especially with more depth) but in general the results we produced were better than  
those comparable to the experiment in the other tests.

"""
# ==============
