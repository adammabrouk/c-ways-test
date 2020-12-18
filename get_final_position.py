
class Robot:
    """
    Cette classe permet de modéliser le comportement du Robot B-VZXR
    """
    def __init__(self, world_file, instructions_file):
        """
        Constructeur de la classe Robot

        Inputs
        ---------
        world_file : str
          chemin d'accès au fichier qui contient les dimensions de l'univers
        instructions_file : str
          chemin d'accès au fichier qui contient les instructions

        Notes
        ---------
        L'abcisse et l'ordonnée du robot sont représentées respectivement par les attributs x et y
        L'orientation de la tête du robot est représentée par l'attribut orient tel que :
            0 => haut, 1 => droite, 2 => bas, 3 => gauche
        """
        self.x            = 0
        self.y            = 0
        self.orient       = 0
        self.w, self.h    = self.get_world_dims_from_file(world_file)
        self.instructions = self.get_instructions_from_file(instructions_file)

    def get_world_dims_from_file(self, world_file):
        """
        Charge les dimensions de l'univers depuis un fichier txt

        Inputs
        -------
        world_file : str
          chemin d'accès au fichier qui contient les dimensions de l'univers

        Returns
        ------
        w : int
          largeur de l'univers
        h : int
          longeur de l'univers
        """
        with open(world_file, "r") as file:
            w, h = list(map(lambda x : x.strip().split(': ')[1], file.readlines()))
        return int(w) , int(h)

    def get_instructions_from_file(self,instructions_file):
        """
        Charge la liste d'instructions depuis un fichier txt

        Inputs
        -------
        instructions_file : str
          chemin d'accès au fichier qui contient la liste d'instructions

        Returns
        ------
        L : [[str,str] ... ]
          Liste des instructions
        """
        with open(instructions_file, "r") as file:
            L = list(map(lambda x : x.strip().split(', '), file.readlines()))
        return L

    def turn(self, direction):
        """
        Change l'orientation du robot selon la direction fournie

        Inputs
        -------
        direction : str (left|right)
        """
        if direction   == 'left':
            self.orient = (self.orient - 1) % 4
        elif direction == 'right':
            self.orient = (self.orient + 1) % 4

    def advance(self, steps):
        """
        Permet au robot d'avancer par [steps] pas dans le sens ou il est orienté
        en tenant en compte le cas ou il rencontre un mur

        Inputs
        -------
        steps : int
          le nombre de pas à avancer

        """
        if self.orient == 0:
            # Partir en haut
            self.y += min(steps, self.h-self.y-1)
        elif self.orient == 1:
            # Partir à Droite
            self.x += min(steps, self.w-self.x-1)
        elif self.orient == 2:
            # Partir en bas
            self.y -= min(steps, self.y)
        elif self.orient == 3:
            # Partir à gauche
            self.x -= min(steps, self.x)

    def start(self):
        """
        Permet au robot d'exécuter séquentiellement toute la liste d'instructions

        Returns
        -------
        (x,y) : tuple(int,int)
          La position finale du Robot

        """
        for instruction in self.instructions:
            direction , steps = instruction[0], int(instruction[1])
            self.turn(direction)
            self.advance(steps)

        # Retourne la position finale
        return (self.x,self.y)

if __name__ == '__main__':
    R         = Robot('universe.txt', 'instrucion_list.txt')
    final_pos = R.start()
    print(final_pos)
