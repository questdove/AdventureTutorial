import items, enemies, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
    """Returns all move actions for adjacent tiles."""
    moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
def available_actions(self):
    """Returns all of the available actions in this room."""
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())
 
    return moves

    

class HomeBase(MapTile):
    def intro_text(self):
        return """ You are at your home."""
    def modify_player(self, player):
        #Room has no actions
        pass

class ClueRoom(MapTile):

    def __init__(self,x,y, item):
        self.item = item
        super().__init(x,y)
    def intro_text(self):
        return """ You are able to sneak into your friend's house.\n It is a complete mess.
                \nDevices and equipment lay scattered everywhere."""

    def add_clue(self, player):
        player.invent.append(self.item)

    def modify_player(self, player):
        self.add_clue(player)

class hostileRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

class corpCopRoom(hostileRoom):
    def __init__(self, x, y):
        super.__init__(x, y, enemies.corpCop())

        def intro_text(self):
            if self.enemy.is_alive():
                return """A Xcorp agent hears you and jumps out with a raised taser baton!"""
            else:
                return """The agent is dead on the ground."""

class placeholderRoom(MapTile):
    def intro_text(self):
        return """
        Here there be nothing but Space, time, and the growing axiety we all are aware of when things go silent
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    

class findClueRoom(clueRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Clue())
 
    def intro_text(self):
        return """
        You notice something peculiar in the butthole.\n
        It's a fucking clue! You pick it up.
        """








    
