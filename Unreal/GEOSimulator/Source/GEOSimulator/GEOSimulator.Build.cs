// Fill out your copyright notice in the Description page of Project Settings.

using System;
using System.IO;
using UnrealBuildTool;

public class GEOSimulator : ModuleRules
{
	public GEOSimulator(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
	
		PublicDependencyModuleNames.AddRange(new string[] {
            "Core", "CoreUObject", "Engine", "InputCore", "Slate", "ProceduralMeshComponent",
            "ImageWrapper", "RenderCore", "JsonUtilities", "Json"
        });


        PrivateDependencyModuleNames.AddRange(new string[] {  });
        
        if(Target.Platform == UnrealTargetPlatform.Mac)
        {
             PublicAdditionalLibraries.Add(Directory.GetParent(ModuleDirectory).Parent.FullName + "/Libs/rpc/lib/librpc.a");
        }
        else if(Target.Platform == UnrealTargetPlatform.Win64)
        {
            PublicAdditionalLibraries.Add(Directory.GetParent(ModuleDirectory).Parent.FullName + "/Libs/rpc/lib/rpc.lib");
        }

        //PublicIncludePaths.Add(Directory.GetParent(ModuleDirectory).Parent.Parent.FullName + "/PluginGEOControl/GEOControl/");
        PublicIncludePaths.Add(Directory.GetParent(ModuleDirectory).Parent.FullName + "/Libs/rpc/include/");

        // Uncomment if you are using Slate UI
        // PrivateDependencyModuleNames.AddRange(new string[] { "Slate", "SlateCore" });

        // Uncomment if you are using online features
        // PrivateDependencyModuleNames.Add("OnlineSubsystem");

        // To include OnlineSubsystemSteam, add it to the plugins section in your uproject file with the Enabled attribute set to true
    }
}

