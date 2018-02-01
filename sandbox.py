
with open("hosts.txt") as hostout:
    for line in hostout:
        with open("stubpout", "a+") as stubout:
            with open("stage_snip.txt", "r") as snip:
                content = snip.read()
                result = content.replace("hostname", line)
                stubout.write(result + "\n")
