import sys

def bar(iteration, total, task_name = ""):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    doing = ""
    if task_name == "":
        doing = "\rPercentage of completion %s%s%s" % ('|/-\\'[iteration % 4], percent, '|/-\\'[iteration % 4])
    else:
        doing = "\rPercentage of completion for task: %s - %s%s%s" % (task_name, '|/-\\'[iteration % 4], percent, '|/-\\'[iteration % 4])
    sys.stdout.write(doing)
    sys.stdout.flush()


'''
import progress_bar
progress_bar.bar(indx, corpus_size)
indx = indx +1

progress_bar.bar(iteration, total_length_if_file, "parsing excel file")
iteration = iteration + 1
'''