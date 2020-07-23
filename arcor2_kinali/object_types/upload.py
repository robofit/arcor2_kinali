#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from arcor2.object_types.upload import upload


def main() -> None:

    upload("arcor2_kinali.object_types.barcode/Barcode")
    upload("arcor2_kinali.object_types.interaction/Interaction")
    upload("arcor2_kinali.object_types.robot/RestRobot")
    upload("arcor2_kinali.object_types.search/Search")
    upload("arcor2_kinali.object_types.statistic/Statistic")


if __name__ == "__main__":
    main()
