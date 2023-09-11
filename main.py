import random


def main() -> None:
  try:
    enOrDec = bool(
      int(
          input("Are you encrypting or Decrypting? 0 for encrypting, \
1 for decrypting.\n>>")))
  except ValueError:
    print("\n\033[91mInvalid input")
    return

  # Random.seed() decides the output for random.randindt().
  # If you use the seed "cheese", random.randint(3) will be random,
  # but will always output the same thing for as long as you use the seed "cheese"
  random.seed(
      input("Enter the " + ("decryption " if enOrDec else "encryption ") +
            "seed\
  \n>>"))

  try:
    text = input("Enter the text\n>>")

    if not text:
      with open("input.txt", "r") as f:
        text = f.read()

    output = [
        chr(ord(c) - random.randint(0, 164))
        if enOrDec else chr(ord(c) + random.randint(0, 164)) for c in text
    ]

  except ValueError:
    print(
        "\n\033[91mMake sure you are decrypting a properly encrypted message.")
    return

  out = ""
  for i in output:
    out += i

  print(out)

  with open("output.txt", "w") as f:
    f.write(out)


main()
