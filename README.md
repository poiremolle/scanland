# scanland
A small Pygame application that allows you to drop in drawings and watch them bounce around the screen atop a virtual landscape. I came across this idea in the spring of 2025 when I volunteered at [Hello Ada's](https://www.helloada.ai/en/) tech festival for kids. [Guldastronaut](https://www.guldastronaut.dk/) had set up a virtual aquarium in the lobby where kids (and many adults!) scanned in drawings of aquatic creatures which then appeared swimming around the screen. I had a lot of fun with it while helping the kids out at this activity and decided I wanted one for my house as well.

I'm not sure how Guldastronaut made theirs, but I went with Python, using the [pillow library](https://pypi.org/project/pillow/) for image processing, Pygame for the display and [watchdog](https://python-watchdog.readthedocs.io/en/stable/index.html) for detecting if an image as been added (so basically any file dropped in the '/assets/creature_images' will be detected, not just images from a scanner)

It could be fun to add a GUI, possibility to change backgrounds, an executable and testing, but for now this will do. :)
