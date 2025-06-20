def checkmate(board_str):
    try:
        board = board_str.strip().split("\n")  # แยกกระดานออกเป็นแถว
        n = len(board)  # ขนาดกระดาน

        # หาตำแหน่งของ King (K)
        king_pos = None
        for i in range(n):
            for j in range(len(board[i])):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos:
                break
        if not king_pos:
            print("Fail")
            return

        ki, kj = king_pos  # ตำแหน่ง King

        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < len(board[x])

        # ตรวจสอบการโจมตีจาก Pawn (โจมตีแนวทแยงข้างหน้า)
        for di, dj in [(-1, -1), (-1, 1)]:
            ni, nj = ki + di, kj + dj
            if in_bounds(ni, nj) and board[ni][nj] == 'P':
                print("Success")
                return

        # ตรวจสอบแนวตรงและแนวนอนสำหรับ Rook และ Queen
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = ki + dx, kj + dy
            while in_bounds(x, y):
                cell = board[x][y]
                if cell == '.':
                    x += dx
                    y += dy
                    continue
                if cell == 'R' or cell == 'Q':
                    print("Success")
                    return
                break

        # ตรวจสอบแนวทแยงสำหรับ Bishop และ Queen
        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in diagonals:
            x, y = ki + dx, kj + dy
            while in_bounds(x, y):
                cell = board[x][y]
                if cell == '.':
                    x += dx
                    y += dy
                    continue
                if cell == 'B' or cell == 'Q':
                    print("Success")
                    return
                break

        print("Fail")  # ถ้าไม่โดนตัวไหนโจมตีเลย
    except Exception:
        pass  # ไม่ทำอะไรถ้าเกิดข้อผิดพลาด