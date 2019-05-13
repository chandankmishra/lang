"""
Paginated API

Problem Description

A third-party API that we're using has a paginated API.  It returns results in
chunks of 10.  This is implemented below on "fetch_page"

We don't think that API is very useful, and would prefer the following an implementation
where only one call to "fetch" will return a given number of results, abstracting away the
need to do pagination.

Your task will be to implement ResultFetcher.fetch()
"""
# Max results from fetch_page for testing fetch implementation
MAX_RESULTS = 103


def fetch_page(page):
    """
    Return the next page of results.  If page == None, starts from the
    beginning.  Otherwise, fetches the next 10 records after the last page.

    returns:
        {
            "results": [...],
            "page": 3
        }
    """
    page = page or 0
    if page * 10 > MAX_RESULTS:
        return {"page": None, "results": []}
    return {
        "page": page + 1,
        "results": range(page * 10, min(MAX_RESULTS, (page + 1) * 10)),
    }


class ResultFetcher:
    def __init__(self):
        self.cache = []
        self.pages_read = 0

    def fetch(self, num_results):
        """
        TO IMPLEMENT
        Return num_results amount of results from fetch_page.
        It should keep a place holder to make the right amount of subsequent
        calls to fetch_page to return the right number of results.
        """
        qlen = len(self.cache)
        if num_results == qlen:
            result = list(self.cache)
            self.cache = []
        elif num_results < qlen:
            result = list(self.cache[:num_results])
            self.cache = self.cache[num_results:]
        else:
            records_to_read = num_results - len(self.cache)
            no_of_records = (records_to_read // 10) + 1
            for _ in range(no_of_records):
                ret = fetch_page(self.pages_read)["results"]
                if len(ret) == 0:
                    break
                self.cache += ret
                self.pages_read += 1
            result = self.cache[:num_results]
            self.cache = self.cache[num_results:]
        return result


def test_case(actual, expected):
    if actual != expected:
        print(f"FAILED: expected {expected}, got {actual}")
    else:
        print("SUCCESS")


if __name__ == "__main__":
    fetcher = ResultFetcher()
    test_case(len(fetcher.fetch(5)), 5)
    test_case(len(fetcher.fetch(11)), 11)
    test_case(len(fetcher.fetch(103)), 87)
    test_case(len(fetcher.fetch(103)), 0)
    test_case(len(fetcher.fetch(200)), 0)

    fetcher = ResultFetcher()
    test_case(len(fetcher.fetch(200)), 103)
