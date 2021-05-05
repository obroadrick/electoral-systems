import numpy as np
import math
import copy
from vs import gt_winner
from vs import default_params
from vs import Smith_set


def gen_preference(mean):
    """ 
    Generates a preference for a candidate with the passed mean.
    A preference is a normally distributed value with mean mean and
    standard deviation 1.
    """
    return np.random.normal(mean,1)

def gen_voter(cand_means):
    """
    Generates a single voter: a list of beliefs.
     - ith entry of voter is preference/belief for ith candidate
    """
    voter = []
    for i in range(len(cand_means)):
        voter.append(gen_preference(cand_means[i]))
    """
    But if they like 1, they like 0 more and dislike 2 more
    if voter[1] > 0:
        voter[0] += .01
        voter[2] -= .01
    """
    return voter

def gen_voters(num_voters, cand_means):
    """ 
    Generates a list of num_voters voters for cand_means candidate means.
    """
    voters = []
    for i in range(num_voters):
        voters.append(gen_voter(cand_means))
    return voters

def plurality(voters):
    """
    Returns the candidate that would win a plurality contest between
    the passed voters if they vote truthfully.
    """
    votes = np.zeros(len(voters[0]))
    for voter in voters:
        votes[np.argmax(voter)] += 1
    return np.argmax(votes)

def gen_ranking(voter):
    """ 
    Returns a ranking for the passed voter.
    A ranking is a list whose ith entry is ith most preferred candidate (integer).
    """
    ranking = []
    for i in range(len(voter)):
        maxidx = np.argmax(voter)
        ranking.append(maxidx)
        voter[maxidx] = -10000000
    return ranking

def gen_rankings(voters):
    """
    Returns a list of rankings for the passed voters.
    """
    rankings = []
    for voter in voters:
        rankings.append(gen_ranking(voter))
    return rankings
 
def instant_runoff(rankings):
    """
    Returns the candidate that would win an instant-runoff contest
    with the passed voters if they vote truthfully.
    """
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

def gen_profile(rankings):
    """
    Returns a profile for the passed rankings.
    A profile is a dict mapping ranking tuples to multiplicities.
    """
    profile = {}
    for ranking in rankings:
        ranking = tuple(ranking)
        if ranking in profile:
            profile[ranking] += 1
        else:
            profile[ranking] = 1
    return profile

def gt_method(rankings):
    """
    Returns the candidate that would win a GT-method contest
    with the passed voters voting truthfully.
    """
    cands = list(range(len(voters[0])))
    profile = gen_profile(rankings)
    election_id = 0
    return gt_winner(cands, profile, default_params(), election_id, False)



#testing: print(gen_profile(gen_rankings([[3,1,5],[9,3,5], [1,0,3]])))

#cand_means = [-1,0,1]
#cand_means = [-.1,0,.1]
#cand_means = [-.01,0,0]
cand_means = [0,0,0]
num_voters = 100000
for i in range(10):
    voters = gen_voters(num_voters, cand_means)
    rankings = gen_rankings(copy.deepcopy(voters))
    print("plurality:", plurality(copy.deepcopy(voters)))
    print("instant-runoff:", instant_runoff(copy.deepcopy(rankings)))
    print("gt-method:", gt_method(copy.deepcopy(rankings)))
    print("Smith set:",str(Smith_set(list(range(len(voters[0]))),
                                            gen_profile(copy.deepcopy(rankings)),
                                            default_params(),
                                            0, 
                                            False)))
    print()




