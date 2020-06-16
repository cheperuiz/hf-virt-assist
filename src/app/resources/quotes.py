from flask import request
from flask_restx import Namespace, Resource
from models.quote_repository import get_all_quotes, save_quote

ns = Namespace("quotes", description="A space to store and retrieve quotes by users... Very useful indeed...")


def fix_quote(quote):
    quote["_id"] = str(quote["_id"])
    quote["created_at"] = str(quote["created_at"])
    return quote


quote_parser = ns.parser()
quote_parser.add_argument("user", type=str, location="json", required=True)
quote_parser.add_argument("quote", type=str, location="json", required=True)


@ns.route("/")
class QuotesList(Resource):
    def get(self):
        all_quotes = get_all_quotes()
        all_quotes = [fix_quote(quote) for quote in all_quotes]
        return all_quotes

    @ns.expect(quote_parser)
    def post(self):
        new_quote = quote_parser.parse_args()
        return save_quote(new_quote)
