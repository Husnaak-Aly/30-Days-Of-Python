# Basic Chatbot

print("***Chandio Chatbot***")
print("""
    => Hi
    => Bye
    => Thanks
    => Help
      """)
command = input("Enter command:").lower().split(" ")

match command:
    case "hi" | "hello" | "hey"| "aoa":
        print("Hi! Sain Chha hal aa? ")
    case "bye" | "yaro yari":
        print("Theek aa po gad")
    case "thanks" | "mehrbani" | "qurb":
        print("Sain pehnji galh aa")
    case "help":
        print("Sain! Man tawhan ji kehri madad kare saghan tho? bas hukum kayo. Tawhan ta pehnja manhu aahyo")
    case _:
        print("Sain galat command likhi athaw inh khe mehrbani kare durust kayo")