def isSearchRange(player, enemy):
    #return true, UnI - enemy.searchR return false only false
    UnI = math.sqrt((player.x - enemy.x) ** 2 + (player.y - enemy.y) ** 2)
    if UnI - enemy.searchR <= 0:
        return True, UnI - enemy.searchR
    else:
        return False,0
