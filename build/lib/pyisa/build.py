import os
import click
from pathlib2 import Path


@click.command()
@click.option('--project_path', help='Absolute path where you want to create'
                                     ' the project root directory')
@click.option('--project_name', help='Name of your project')
@click.option('--tree', default=True, help='Is project structure'
                                                   ' visualization needed')
def build_project(project_path, project_name, tree=True):
    """
    Creates a basic project structure for Data Science projects.
    
    Parameters:
    -----------
        project_path: str - Absolute path where you want to create the project
                            root directory
        project_name: str - Name of your project
        tree: bool - Whether a tree visualization is required. Defaults
                             to True
        
    Returns:
    --------
        None. Creates required directories and sub-directories for a basic Data
              Science project
        
    Example:
    --------
        build_project --project_path=/absolute/path --project_name=name
        --project_tree=True
    """
    project_path = Path(project_path)
    os.chdir(str(project_path))
    if Path(project_name).exists() and Path(project_name).is_dir():
        print 'Project already exists'
    else:
        folder = project_path.joinpath(project_name)
        folder.mkdir(mode=0777, parents=True)     
        proj_path = project_path.joinpath(project_name)
        os.chdir(str(proj_path.absolute()))
        fol_ls = ['models', 'data', 'preprocess', 'visualize', 'results']
        fil_ls = ['README.md', 'utils.py', 'requirements.txt', '__init__.py']
        for fol in fol_ls:
            proj = proj_path.joinpath(fol)
            proj.mkdir(mode=0777, parents=True)
        for fil in fil_ls:
            files = proj_path.joinpath(fil)
            files.touch(mode=0777)
        for fol in fol_ls:
            proj = proj_path.joinpath(fol)
            os.chdir(str(proj.absolute()))
            readme_file = proj.joinpath('README.md')
            readme_file.touch(mode=0777)
            if fol == 'models' or fol == 'preprocess':
                init_file = proj.joinpath('__init__.py')
                init_file.touch(mode=0777) 
            if fol == 'visualize':
                init_file = proj.joinpath('__init__.py')
                init_file.touch(mode=0777)
                image = proj.joinpath('Images')
                image.mkdir(mode=0777, parents=True)
                os.chdir(str(image.absolute()))
                readme_file = image.joinpath('README.md')
                readme_file.touch(mode=0777)
    if tree:
        project_tree(project_path.joinpath(project_name))
                

def project_tree(project_path, branch='   |---- '):
    """
    Creates a tree diagram of the project structure
    
    Parameters:
    -----------
        project_path: str - Absolute path where you want to create the project
                            root directory
        branch: str - How do you want to visualize the branch separation.
                      Defaults to '   |---- '
        
    Returns:
    --------
        None. Prints a tree diagram of the project structure
        
    Example:
    --------
        project_tree(project_path='/absolute/path', branch='   |---- ')
    """
    dir_ls = str(project_path).split('/')
    file_list = sorted(list(project_path.rglob('*')))
    print project_path.stem
    for files in file_list:
        depth = len([j for j in str(files).split('/') if len(j) > 0])
        last = [j for j in str(files).split('/') if len(j) > 0][-1]
        marker = {False: '', True: '/'}[Path(files).is_dir()]
        print branch*(depth-(len(dir_ls) - 1)) + last + marker


if __name__ == '__main__':
    build_project()
