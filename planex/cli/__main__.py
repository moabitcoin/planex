import csv
import argparse
import collections
from pathlib import Path

import toml
import osmium


# Known issues:
#  - no location information
#  - no relation information
#  - everything is normalized


# https://docs.osmcode.org/pyosmium/latest/
class SegmentHandler(osmium.SimpleHandler):
    def __init__(self, writer, layers):
        super().__init__()

        self.writer = writer
        self.layers = layers

    def way(self, w):
        noderefs = list(w.nodes)
        segments = self._segments(noderefs)

        wid = w.positive_id()
        ts = w.timestamp.isoformat()
        tags = [(k, v) for k, v in w.tags]

        for (k, v) in tags:
            if (k, v) not in self.layers:
                continue

            for (s, t) in segments:
                self.writer.writerow([wid, s, t, k, v, ts])

    def _segments(self, w):
        return [w[i+0:i+2] for i in range(len(w) - 1)]


class PackageWriter:
    def __init__(self, fp, version):
        self.writer = csv.writer(fp)
        self.version = version

    def writerow(self, row):
        self.writer.writerow([self.version] + list(row))


class Layers:
    def __init__(self, path):
        config = toml.load(path)

        self.tags = collections.defaultdict(set)

        for key, vals in config["layers"].items():
            self.tags[key].update(vals)

    def __contains__(self, tag):
        k, v = tag

        if "*" in self.tags[k]:
            return True

        if v in self.tags[k]:
            return True

        return False


def main(args):
    layers = Layers(args.layers)

    with args.pkg.open("w") as fp:
        writer = PackageWriter(fp, args.version)

        handler = SegmentHandler(writer, layers)
        handler.apply_file(str(args.map))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PlanEx")
    arg = parser.add_argument

    arg("map", type=Path, help="path to base map .osm.pbf to read from")
    arg("pkg", type=Path, help="path to package .pkg to write to")
    arg("--layers", required=True, type=Path, help="path to layers definition file")
    arg("--version", required=True, type=int, help="map version embedded in package")

    main(parser.parse_args())
