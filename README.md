# electoral-systems

This repository contains my work for a project in my Game Theory in Computer Science course at GWU. The project presentation (`project_presentation.pdf`) is included, as well as the source code for running simulations of elections to compare three electoral systems: plurality, instant-runoff voting, and the GT-Method. 

## GT-Method
As presented in [An Optimal Single-Winner Preferential Voting System Based on
Game Theory](https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/rivest.pdf), the GT-Method is a really interesting approach to the problem of choosing a winner of an election using a pool of ballots, rankings of the candidates in order of preference. The GT-Method frames the choice as a game. Suppose two voting-systems would choose a different candidate, then whichever system selects the candidate who would win between the two in a head-to-head election wins the margin of that theoretical electino as its payoff. Imagine playing this game over and over, and an optimal strategy emerges in the form of a probability distribution ofver the candidates. For example, if there is a Condorcet winner (one who beats all other candidates in a head-to-head contest), then the distribution is simply 1 for that candidate, and 0 ffor all others. Clearly this is thte most optimal strategy because any other candidate loses to this candidate. Such an optimal strategy always exists, and we can find it by solving a simple linear programming problem.
### Downsides
Perhaps a downside to the GT-Method is that a winner to the election is chosen by random chance whenever a Condorcet tie exists. Rivest and Shen argue that a public 'tie-breaking ceremony' could be used, and they point out that random chance has been used in some small contest decisions in before. While random chance does achieve optimality, it may be difficult to become popular on a large scale because a deterministic choice feels a bit more natural and fair regardless of what the math says.

## Results
There were cases in which a plurality election failed to select the most popular candidate, while the others did so.
