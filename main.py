def main(data: bytes = b"OK") -> str:
    try:
        text = data.decode("utf-8")
        if text == "OK":
            return "OK"
        else:
            return "NOT OK"
    except UnicodeDecodeError:
        return "NOT OK"


if __name__ == "__main__":
    print(main(b"OK"))
