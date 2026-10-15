# command = ["move", "north",]

# match command:
#     case ["quit"]:
#         print("Goodbye!")
#     case ["move", direction]:
#         print(f"Moving towards {direction}")
#     case ["teleport", x, y]:
#         print(f"Jumping to coordinates {x}, {y}")
#     case _:
#         print("Unknown command")



response = {"status": "error", "details": {"code": 500, "msg": "Server Crash"}}

match response:
    case {"status": "success", "data": payload}:
        print(f"Data received: {payload}")
    case {"status": "error", "details": {"code": code, "msg": message}}:
        print(f"Error {code}: {message}")

