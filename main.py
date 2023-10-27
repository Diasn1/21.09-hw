try:
    def can_king_move(x1, y1, x2, y2):
        if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
            raise ValueError("Координаты должны быть в интервале от 1 до 8")

        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

    figure_choice = input("Выберите фигуру (король/ладья): ").lower()
    
    if figure_choice == "король":
        king_x1 = int(input("Введите номер столбца короля (1-8) на первой клетке: "))
        king_y1 = int(input("Введите номер строки короля (1-8) на первой клетке: "))
        king_x2 = int(input("Введите номер столбца короля (1-8) на второй клетке: "))
        king_y2 = int(input("Введите номер строки короля (1-8) на второй клетке: "))
        
        if can_king_move(king_x1, king_y1, king_x2, king_y2):
            print("YES")
        else:
            print("NO")
    
    elif figure_choice == "ладья":
        rook_x = int(input("Введите номер столбца ладьи (1-8): "))
        rook_y = int(input("Введите номер строки ладьи (1-8): "))
        figure_x = int(input("Введите номер столбца другой фигуры (1-8): "))
        figure_y = int(input("Введите номер строки другой фигуры (1-8): "))
        
        if rook_x == figure_x or rook_y == figure_y:
            print("YES")
        else:
            print("NO")
    
    else:
        raise ValueError("Выбрана недопустимая фигура. Выберите 'король' или 'ладья'.")

except ValueError as e:
    print(f"Ошибка: {e}. Пожалуйста, введите правильные данные.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
