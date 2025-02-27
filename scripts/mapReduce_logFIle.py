from mrjob.job import MRJob
import sys

class PeakTraffic(MRJob):

    def mapper(self, _, line):
        fields = line.strip().split(",")

        # Skip header and invalid lines
        if len(fields) < 2 or fields[0].strip().lower() == "ip":
            return

        try:
            timestamp_parts = fields[1].strip().split(":")  # Extract time parts
            if len(timestamp_parts) > 1:
                hour = timestamp_parts[1]  # Extract hour correctly
                yield hour, 1
        except IndexError:
            sys.stderr.write("Skipping malformed line: {}\n".format(line))
        except Exception as e:
            sys.stderr.write("Error processing line: {} | Error: {}\n".format(line, str(e)))

    def reducer(self, key, values):
        yield key, sum(values)

if name == 'main':
    PeakTraffic.run()