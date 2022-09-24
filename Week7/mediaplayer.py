from random import randint

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


class Dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, title, artist):
        node = Song(title, artist)
        if (self.head is None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def delete(self, title):
        current = self.head
        prev = self.head
        while current:
            if (current.title == title):
                prev.next = None
                self.tail = prev
            elif (current == self.head):
                current.next.prev = None
                self.head = current.next
            else:
                prev.next = current.next
                current.next = prev
            return
        prev = current
        current = current.next

    def skip(self):
        current = self.head
        val = current.next
        return val
        

    def play(self):
        return self.head.title + ' by ' + self.head.artist

    def print(self):
        for node in self.iter():
            print(' - ', node)

    
    def iter(self):
        current_title = self.head
        current_artist = self.head
        while current_title:
            iter_title = current_title.title
            iter_artist = current_artist.artist
            current_title = current_title.next
            current_artist = current_artist.next
            yield iter_title + ' by ' + iter_artist





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


link = Dll()

link.add('Sunset', 'The Midnight')
link.add('Retrograde', 'Silverstein')
link.add('A Midwestern State of Emergency', 'Silverstein')
link.add('In Dying Days', 'As Blood Runs Black')
link.add('Carrion', 'Parkway Drive')
link.add('The City Sleeps in Flames', 'Scary Kids Scaring Kids')



while True:
    menu()
    choice = int(input())

    if choice == 1: # DONE
        title = input("Song Title: ")
        artist = input("Song Artist: ")
        link.add(title, artist)
        print("New Song Added to Playlist")

    elif choice == 2:
        print("You list currently includes: ")
        current_list = link.print()
        link.delete(input('Title to remove: '))
        print("Song Removed from Playlist")

    elif choice == 3: # DONE
        play = link.play()
        print("Playing....", play)

    elif choice == 4:
        skip = link.skip()
        print("Skipping....", skip)

    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....") 

    elif choice == 6:
        print("Shuffling....") 
        shuffle = link.shuffle()

    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")

    elif choice == 8: # DONE
        print("Song List: ")
        ord = link.print()

    elif choice == 0:
        print("Goodbye.")
        break

            