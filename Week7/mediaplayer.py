
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other): #equal
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other): #not equal
        return not (self == other)

    def __lt__(self, other): #less than 
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other): #greater than
        return ((self.title, self.artist) < (other.title, other.artist))
        

class DoublylinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
    
    def addFirst(self, title, artist) -> None:
        new_song = Song(title, artist)
        if (self.head == None):
            self.head = new_song
            self.tail = new_song
            print("41", self.head)
        else:
            new_song.next = self.head
            self.head.prev = new_song
            self.head = new_song
            print('46',self.head)
    
    def remove(self, title) -> None:
        current = self.head
        prev = self.head
        while current:
            if current.title == title:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                    print('56',self.head)
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                    print('59',self.head)
                else:
                    prev.next = current.next
                    current.next = prev
                    print('62',self.head)
                return
            prev = current
            current = current.next
    
    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.title
            current = current.next
            yield val
    

    
    









def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


link = DoublylinkedList()

link.addFirst('Sunset', 'The Midnight')
link.addFirst('Retrograde', 'Silverstein')
link.addFirst('A Midwestern State of Emergency', 'Silverstein')
link.addFirst('In Dying Days', 'As Blood Runs Black')
link.addFirst('Carrion', 'Parkway Drive')
link.addFirst('The City Sleeps in Flames', 'Scary Kids Scaring Kids')








# while True:
#     menu()
#     choice = int(input())

#     if choice == 1:
#         add_title = input("Song Title: \n")
#         add_artist = input("Song Artist: \n")
#         link.addFirst(add_title, add_artist)
#         print("New Song Added to Playlist")

#     elif choice == 2:
#         remove_title = input("Song Title: \n")
#         link.remove(remove_title)
#         print("Song Removed to Playlist")

#     elif choice == 3:
#         # Play the playlist from the beginning
#         # Display song name that is currently playing
#         print("Playing....")

#     elif choice == 4:
#         # Skip to the next song on the playlist
#         # Display song name that is now playing
#         print("Skipping....")

#     elif choice == 5:
#         # Go back to the previous song on the playlist
#         # Display song name that is now playing
#         print("Replaying....") 

#     elif choice == 6:
#         # Randomly shuffle the playlist and play the first song
#         # Display song name that is now playing
#         print("Shuffling....") 

#     elif choice == 7:
#         # Display the song name and artist of the currently playing song
#         print("Currently playing: ", end=" ")

#     elif choice == 8:
#         # Show the current song list order
#         print(f"\nSong list: \n")

#     elif choice == 0:
#         print("Goodbye.")
#         break

            