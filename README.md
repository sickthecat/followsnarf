# followsnarf - follow who?


The script is a Python command-line utility designed to retrieve the accounts followed by a target Twitter user using the Twitter API v1.1 with Bearer Token authentication. It allows you to provide a single Twitter username or a list of usernames in a text file, and it will display the accounts that each user follows.

Here's how the script works:

1. The script takes command-line arguments to specify the target Twitter user(s) and the Bearer Token for API authentication.
2. You can provide the target Twitter user(s) in two ways:
   - As a single username directly in the command line: `python script.py target_username --bearer_token YOUR_BEARER_TOKEN`
   - As a list of usernames stored in a text file: `python script.py --file accounts.txt --bearer_token YOUR_BEARER_TOKEN`
   (Replace "target_username" with the Twitter username and "YOUR_BEARER_TOKEN" with the actual Bearer Token.)
3. The script will then attempt to retrieve the accounts followed by the provided Twitter user(s) using the Twitter API v1.1.
4. If successful, it will display the list of followed accounts for each user.

How to use it in a GitHub README:

1. Save the script in your GitHub repository (e.g., as `followsnarf.py`).
2. In your GitHub README, explain what the script does and how it can be used.
3. Provide clear instructions on how to use the script with examples:
   - Explain the command-line arguments the script requires (target_username or --file and --bearer_token).
   - Show examples of how to use the script to retrieve the followed accounts for specific Twitter users.

Here's an example of how to include the script in your GitHub README:

```
## Twitter FollowSnarf

Twitter FollowSnarf is a Python script that allows you to retrieve the accounts followed by a Twitter user using the Twitter API v1.1 with Bearer Token authentication.

### How to use

1. Clone this repository to your local machine.
2. Install the required libraries: `pip install requests argparse`
3. Run the script with the following command:

```bash
python followsnarf.py target_username --bearer_token YOUR_BEARER_TOKEN
```

or

```bash
python followsnarf.py --file accounts.txt --bearer_token YOUR_BEARER_TOKEN
```

Replace "target_username" with the Twitter username you want to investigate and "YOUR_BEARER_TOKEN" with your actual Bearer Token.

If the Twitter user is public and the provided Bearer Token is valid, the script will display the list of accounts followed by the target user.

### Example

```bash
python followsnarf.py realDonaldTrump --bearer_token AAAAAAAAAAAAAAAAAAAANALANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA
```

Output:
```
The account 'realDonaldTrump' follows: FoxNews, seanhannity, DanScavino, DiamondandSilk, TuckerCarlson, Parscale, DailyCaller, Varneyco, dbongino, IngrahamAngle, TrumpGolf, WhiteHouse, FoxBusiness, Mike_Pence, Trump, TrumpHotels, TrumpCharlotte, TrumpChicago, TrumpLasVegas, TrumpDC, TrumpGolfLA, TrumpNewYork, TrumpDoral, TrumpGolfDC, TrumpTurnberry, TrumpScotland, TrumpIreland, TrumpVanessa, TrumpResorts, LaraLeaTrump, TrumpGolfEric, TrumpOrganization, EricTrump, TrumpFoundation, Trump
