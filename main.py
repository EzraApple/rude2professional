import sys
import api_call


def main(prompt):
    print(prompt)
    key = "YOUR KEY HERE"
    response = api_call.get_response(prompt, key)
    print(response)


if __name__ == "__main__":
    main(sys.argv[1])

