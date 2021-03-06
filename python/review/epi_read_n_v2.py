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
        self.total_record = 0
        self.curr_record = 0
        self.cache = []
        self.result_index = -1
        self.last_page = 0
        self.record_sent = 0
        self.max_records = MAX_RESULTS

    def fetch(self, num_results):
        """
        TO IMPLEMENT
        Return num_results amount of results from fetch_page.
        It should keep a place holder to make the right amount of subsequent
        calls to fetch_page to return the right number of results.
        """
        if self.record_sent >= num_results or self.record_sent >= self.max_records:
            return []
        elif self.record_sent < num_results <= self.total_record:
            total = self.total_record - self.record_sent
            to_send = num_results - self.record_sent

            result = self.cache[:tosend]
            self.cache = self.cache[tosend:]
        else:
            num_results += self.record_sent
            if num_results > self.max_records:
                num_results = self.max_records

            records_to_fetch = num_results - self.total_record  # 1
            no_of_calls = (records_to_fetch // 10) + 1
            to_send = records_to_fetch + self.total_record - self.record_sent

            # update the cache
            for _ in range(no_of_calls):
                self.cache += fetch_page(self.last_page)["results"]
                self.last_page += 1
                self.total_record += 10
                self.record_sent = num_results

            result = self.cache[0:to_send]
            self.cache = self.cache[to_send:]
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
