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
        self.current = None
        self.count = 0

    def add(self, title, artist):
        node = Song(title, artist)
        if (self.head is None):
            self.head = node
            self.tail = node
            self.current = node
            self.count += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.current = self.head
            self.count += 1
    
    def delete(self, title): 
        if self.head is None: 
            print("Playlist is empty.")
            return
        
        if self.head.next is None:
            if self.head.title == None:
                self.head = None
                self.currnt = None
                self.count -= 1
            else:
                print("Item not found.")
            return
        
        if self.head.title == title:
            self.current = self.head.next
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return
        
        h = self.head
        while h.next is not None:
            if h.title == title:
                break
            h = h.next
        
        if h.next is not None:
            h.prev.next = h.next
            h.next.prev = h.prev
            self.current = h.next
            self.count -= 1
        else:
            if h.title == title:
                h.prev.next = None
                self.count -= 1
            else:
                print("Song not found.")

    def skip(self): # Traverses forward but skips the head. 
        current = self.current.next 
        if not current:
            current = self.head
            self.current.next = current.next
        self.current = current
        return current

    def goBack(self): # Traverses backwards, but skips the tail.
        current = self.current.prev
        if not current:
            current = self.tail
            self.current.prev = current.prev
        self.current = current
        return current
    
    def displayCurrentSong(self):
        return self.current

    def shuffle(self):
        if (self.head is None):
            raise Exception("Not enough songs added to playlist to shuffle.")
        else:
            current = self.head
            while (current is not None):
                length = (self.count - 1)
                random_index = randint(0, length)
                random_node = self.getNodeIndex(random_index)
                current.title, random_node.title = random_node.title, current.title
                current.artist, random_node.artist = random_node.artist, current.artist
                current = current.next

    def getNodeIndex(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current
        

    def play(self):
        return self.current

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

    elif choice == 2: # DONE
        print("You list currently includes: ")
        current_list = link.print()
        link.delete(input('Title to remove: '))
        print("Song Removed from Playlist")

    elif choice == 3: # DONE
        play = link.play()
        print("Playing....", play)

    elif choice == 4: # DONE
        skip = link.skip()
        print("Skipping....", skip)

    elif choice == 5: # DONE
        goBack = link.goBack()
        print("Replaying....", goBack)
        

    elif choice == 6:
        print("Shuffling....")
        print(link.shuffle())


    elif choice == 7: # DONE
        display = link.displayCurrentSong()
        print("Currently playing: ", end=" ")
        print(display)

    elif choice == 8: # DONE
        print("Song List: ")
        ord = link.print()

    elif choice == 0:
        print("Goodbye.")
        break

            