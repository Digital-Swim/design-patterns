from abc import ABC, abstractmethod

# --- Subject Interface ---
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# --- Real Subject ---
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading image '{self.filename}' from disk...")

    def display(self):
        print(f"Displaying image: {self.filename}")

# --- Proxy ---
class ImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image: RealImage | None = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

# --- Client Code ---
if __name__ == "__main__":
    image1 = ImageProxy("photo1.png")
    image2 = ImageProxy("photo2.png")

    # First access triggers loading
    image1.display()
    image1.display()  # Second call uses already loaded object

    image2.display()
