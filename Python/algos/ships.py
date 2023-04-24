from typing import List

def getNumberofHitsSunks(ships, strikes):
    sunks, hits = 0, 0
    ships = ships.split(',')
    strikes = strikes.split(',')
    for ship in ships:
        ship = ship.split()
        allStrikes = [str(i) + chr(j) for j in range(ord(ship[0][1]), ord(ship[1][1])+1)
                      for i in range(int(ship[0][0]), int(ship[1][0])+1)]
        n = len(allStrikes)
        remains = set(allStrikes) - set(strikes)
        if len(remains) == 0:
            sunks += 1
        elif len(remains) < n:
            hits += 1
    return sunks, hits


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()

    n = len(people)
    left = 0
    right = len(people)-1
    results = []
    num_boats = 0

    while left <= right:
        if left == right:
            num_boats += 1
            results.append([people[right]])
            break

        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            num_boats += 1
            results.append([people[left], people[right]])
        else:
            results.append([people[right]])
            right -= 1
            num_boats += 1

    return num_boats, results


if __name__ == '__main__':
    #sunks, hits = getNumberofHitsSunks("1A 2B,2C 4D", "2A,3B,1A,2B,1B,4C")
    people = [2, 4, 5, 3, 1, 2, 1]
    limit = 5
    num_boats, results = numRescueBoats(people, limit)
    print(num_boats)
    print(results)
    print()
