# Imported module for doing math
import caden_marek_area


def selection():  # Menu that lets the user pick an option
    print('-<>---<>---<>---<>---<>-')
    print('      SELECT SHAPE')
    print('-<>---<>---<>---<>---<>-')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))

    return shape


# Main will call the shape the user selects and will loop until the user wants to end the program
def main():
    while True:
        shape = selection()

        if shape == 1:
            radius = float(input('Circle radius: '))
            caden_marek_area.area_circle(radius)
        elif shape == 2:
            var = float(input('Rectangle length: '))
            var1 = float(input('Rectangle width: '))
            caden_marek_area.area_rectangle(var, var1)
        elif shape == 3:
            var = float(input('Square length: '))
            caden_marek_area.area_square(var)
        elif shape == 4:
            var = float(input('Triangle base: '))
            var1 = float(input('Triangle height: '))
            caden_marek_area.area_triangle(var, var1)

        loop = input('Continue (y/n): ').strip().lower()

        while loop not in ('y', 'n'):
            loop = input('Enter ‘y’ or ‘n’: ').strip().lower()

        if loop == 'n':
            print('PROGRAM DONE')
            break


if __name__ == '__main__':
    main()
