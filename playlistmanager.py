class playlist:
    

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"playlist '{self.name}' ({self.genre}) is ready!")


    def add_song(self, song):
            self.songs.append(song)
            print(f"'{song}'added to {self.name}.")


    def remove_song(self,song):
            if song in self.songs:
                self.songs.remove(song)
                print(f"{song} removed")
            else:
                print(f"{song} not found in playlist")


    def display(self):
            print(f"--- {self.name} {self.genre} ---")
            if self.songs:
                for i,song in enumerate(self.songs, 1):
                    print(f" {i}. {song}")
            else:
                print("no song yet add some")

    def __del__(self):
            print(f"playlist {self.name} has been deleted")        



my_playlist = playlist("road trip mix", "pop")


while True:
    print(" 1. add song 2. remove song 3. view playlist 4. delete & quit")
    choice = input("entre your choice:")
    
    if choice == "1":

       song = input("Enter song name: ")

       my_playlist.add_song(song)

    elif choice == "2":

        song = input("Enter song to remove: ")

        my_playlist.remove_song(song)

    elif choice == "3":

        my_playlist.display()

    elif choice == "4":

        del my_playlist # Destructor fires here

        break

    else:

        print("Invalid choice. Enter 1, 2, 3, or 4.")