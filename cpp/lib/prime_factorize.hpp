#include <vector>

using namespace std;

vector<pair<long long, long long>> prime_factorize(long long n)
{
    vector<pair<long long, long long>> ret;
    long long e = 0;
    for (long long i = 2; i < n; ++i)
    {
        if (i * i > n)
            break;
        if (n % i == 0)
        {
            while (n % i == 0)
            {
                n /= i;
                ++e;
            }
        }
        ret.emplace_back(make_pair(i, e));
        e = 0;
    }
    if (n!=1) ret.emplace_back(make_pair(n,1));
    return ret;
}