from interpork import Window

if __name__ == "__main__":
    window = Window()

    window.SetTitle("Hello Pork!")
    window.SetSize(400, 300)
    # window.SetPosition(0, 0)

    window.Run()
