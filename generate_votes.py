import numpy as np
import math

def gen_preference(mean):
    return np.random.normal(mean,1)

def gen_voter(cand_means):
    voter = []
    for i in range(len(cand_means)):
        voter.append(gen_preference(cand_means[i]))
    return voter

def gen_voters(num_voters, cand_means):
    voters = []
    for i in range(num_voters):
        voters.append(gen_voter(cand_means))
    return voters

def plurality(voters):
    """
    Returns the candidate that would win a plurality contest between
    the passed voters.
    """
    votes = np.zeros(len(voters[0]))
    for voter in voters:
        votes[np.argmax(voter)] += 1
    return np.argmax(votes)

def gen_ranking(voter):
    """ 
    Returns a ranking for the passed voter.
    """
    ranking = []
    for i in range(len(voter)):
        maxidx = np.argmax(voter)
        ranking.append(maxidx)
        voter[maxidx] = -10000
    return ranking

def gen_rankings(voters):
    """
    Returns a list of rankings for the passed voters.
    """
    rankings = []
    for voter in voters:
        rankings.append(gen_ranking(voter))
    return rankings
 
def instant_runoff(voters):
    """
    Returns the candidate that would win an instant-runoff contest
    between these voters if they vote truthfully.
    """
    rankings = gen_rankings(voters)
    maj = math.ceil(len(voters) / 2)

    # Loop until the winning candidate is returned
    while True:
        # Array w how many first votes each candidate got
        first_votes = np.zeros(len(voters[0])) 
        for ranking in rankings:
            first_votes[ranking[0]] += 1

        # If a candidate has a majority of the first votes, they win
        most = max(first_votes)
        if most >= maj:
            return np.argmax(first_votes)

        # Remove first votes for the candidate with the least first votes
        # Determine candidate with the least first votes 
        least_cand = np.argmin(first_votes)
        for ranking in rankings:
            ranking.remove(least_cand)

#cand_means = [-1,0,1]
#cand_means = [-.1,0,.1]
cand_means = [-.01,0,.01]
num_voters = 10000
for i in range(10):
    voters = gen_voters(num_voters, cand_means)
    print("plurality:", plurality(voters))
    print("instant-runoff:", instant_runoff(voters))






